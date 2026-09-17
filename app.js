/**
 * Maths30 — 30-Day NEET/JEE Calculation Skill Training Web App
 * Pure client-side application logic, timers, answer evaluation, persistence, and graphs.
 */

(function() {
  'use strict';

  // ========================================================
  // STORAGE KEYS & DATA STATE
  // ========================================================
  const STORAGE_KEYS = {
    COMPLETED: 'maths_completed_exercises_v1',
    ACTIVE_EXERCISE: 'maths_active_exercise_v1',
    BOOKMARKS: 'maths_bookmarks_v1',
    MISTAKES: 'maths_mistakes_v1',
    SETTINGS: 'maths_settings_v1'
  };

  // State
  let state = {
    currentView: 'dashboard',
    activeExercise: null,      // Current exercise object from EXERCISES_DATA
    currentQIndex: 0,          // 0 to 14
    
    // In-progress exercise runtime state:
    sessionData: {
      exerciseId: null,
      answers: {},             // { [qIndex]: string | number }
      timings: {},             // { [qIndex]: seconds }
      correctStatus: {},       // { [qIndex]: boolean }
      totalElapsedSecs: 0,
      isPaused: false
    },

    // Timers
    qTimerInterval: null,
    qStartTime: 0,
    qElapsedCurrentMs: 0,
    
    exTimerInterval: null,
    exStartTime: 0,
    exElapsedBaseSecs: 0,
    
    // Persistent caches
    completedMap: {},          // { [exerciseId]: summary }
    bookmarksSet: new Set(),   // Set of question IDs
    mistakesList: [],          // Array of mistake objects
    settings: {
      theme: 'dark',
      unlockAll: false
    },

    // UI filters
    tierFilter: 'all',
    mistakesFilter: 'all',
    analyticsMetric: 'totalTime'
  };

  // ========================================================
  // INITIALIZATION
  // ========================================================
  function init() {
    loadPersistentData();
    applyTheme(state.settings.theme);
    setupEventListeners();
    setupKeyboardShortcuts();
    renderDashboard();
    checkResumeBanner();
    
    // Initialize KaTeX render on document
    renderAllMath();
  }

  // Load from localStorage
  function loadPersistentData() {
    try {
      const comp = localStorage.getItem(STORAGE_KEYS.COMPLETED);
      if (comp) state.completedMap = JSON.parse(comp);

      const bmarks = localStorage.getItem(STORAGE_KEYS.BOOKMARKS);
      if (bmarks) state.bookmarksSet = new Set(JSON.parse(bmarks));

      const mists = localStorage.getItem(STORAGE_KEYS.MISTAKES);
      if (mists) state.mistakesList = JSON.parse(mists);

      const sett = localStorage.getItem(STORAGE_KEYS.SETTINGS);
      if (sett) state.settings = Object.assign(state.settings, JSON.parse(sett));
      
      const active = localStorage.getItem(STORAGE_KEYS.ACTIVE_EXERCISE);
      if (active) {
        state.sessionData = JSON.parse(active);
      }
    } catch (e) {
      console.error('Error loading localStorage data:', e);
    }

    updateBadges();
  }

  function saveCompletedMap() {
    try {
      localStorage.setItem(STORAGE_KEYS.COMPLETED, JSON.stringify(state.completedMap));
    } catch (e) { console.error(e); }
  }

  function saveBookmarks() {
    try {
      localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(Array.from(state.bookmarksSet)));
      updateBadges();
    } catch (e) { console.error(e); }
  }

  function saveMistakes() {
    try {
      localStorage.setItem(STORAGE_KEYS.MISTAKES, JSON.stringify(state.mistakesList));
      updateBadges();
    } catch (e) { console.error(e); }
  }

  function saveSettings() {
    try {
      localStorage.setItem(STORAGE_KEYS.SETTINGS, JSON.stringify(state.settings));
    } catch (e) { console.error(e); }
  }

  function saveActiveSession() {
    try {
      if (state.activeExercise && state.sessionData.exerciseId) {
        localStorage.setItem(STORAGE_KEYS.ACTIVE_EXERCISE, JSON.stringify(state.sessionData));
      } else {
        localStorage.removeItem(STORAGE_KEYS.ACTIVE_EXERCISE);
      }
    } catch (e) { console.error(e); }
  }

  function clearActiveSession() {
    state.sessionData = {
      exerciseId: null,
      answers: {},
      timings: {},
      correctStatus: {},
      totalElapsedSecs: 0,
      isPaused: false
    };
    try {
      localStorage.removeItem(STORAGE_KEYS.ACTIVE_EXERCISE);
    } catch (e) { console.error(e); }
  }

  function updateBadges() {
    const mistBadge = document.getElementById('badge-mistakes');
    if (mistBadge) {
      const unsolved = state.mistakesList.filter(m => !m.resolved).length;
      mistBadge.textContent = unsolved;
      mistBadge.dataset.count = unsolved;
      mistBadge.style.display = unsolved > 0 ? 'inline-block' : 'none';
    }

    const bmarkBadge = document.getElementById('badge-bookmarks');
    if (bmarkBadge) {
      const count = state.bookmarksSet.size;
      bmarkBadge.textContent = count;
      bmarkBadge.dataset.count = count;
      bmarkBadge.style.display = count > 0 ? 'inline-block' : 'none';
    }
  }

  // ========================================================
  // THEME SWITCHER
  // ========================================================
  function applyTheme(theme) {
    state.settings.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    const themeIcon = document.getElementById('theme-icon');
    if (themeIcon) {
      themeIcon.textContent = theme === 'dark' ? '🌙' : '☀️';
    }
    saveSettings();
  }

  function toggleTheme() {
    const nextTheme = state.settings.theme === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme);
    showToast(`Switched to ${nextTheme} mode`);
    if (state.currentView === 'analytics') {
      renderProgressGraph();
    }
  }

  // ========================================================
  // NAVIGATION & VIEW CONTROLLER
  // ========================================================
  function navigateTo(viewId) {
    if (state.currentView === 'exercise' && viewId !== 'exercise') {
      // Save current timing when leaving arena
      pauseQuestionTimer();
      saveActiveSession();
    }

    state.currentView = viewId;

    // Update active nav tabs
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.view === viewId);
    });

    // Hide all views, display targeted view
    document.querySelectorAll('.view').forEach(view => {
      view.classList.remove('active');
    });

    const target = document.getElementById(`view-${viewId}`);
    if (target) target.classList.add('active');

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Refresh specific view data
    if (viewId === 'dashboard') {
      renderDashboard();
      checkResumeBanner();
    } else if (viewId === 'analytics') {
      renderAnalytics();
    } else if (viewId === 'mistakes') {
      renderMistakesView();
    } else if (viewId === 'bookmarks') {
      renderBookmarksView();
    }

    renderAllMath();
  }

  // ========================================================
  // DASHBOARD CONTROLLER
  // ========================================================
  function renderDashboard() {
    if (typeof EXERCISES_DATA === 'undefined') return;

    // Calculate global stats
    const totalExercises = EXERCISES_DATA.length; // 30
    const completedIds = Object.keys(state.completedMap).map(Number);
    const completedCount = completedIds.length;
    
    let totalQuestionsSolved = 0;
    let totalCorrect = 0;
    let totalTimeSecs = 0;
    let totalRecordedQuestions = 0;

    completedIds.forEach(id => {
      const rec = state.completedMap[id];
      if (rec) {
        totalQuestionsSolved += 15;
        totalCorrect += (rec.score || 0);
        totalTimeSecs += (rec.totalTimeSecs || 0);
        if (rec.questionTimings) {
          totalRecordedQuestions += Object.keys(rec.questionTimings).length;
        }
      }
    });

    const overallAccuracy = totalQuestionsSolved > 0 
      ? ((totalCorrect / totalQuestionsSolved) * 100).toFixed(1) 
      : 0;

    const avgTimeSecs = totalQuestionsSolved > 0 
      ? (totalTimeSecs / totalQuestionsSolved).toFixed(1) 
      : '--';

    const currentDay = Math.min(completedCount + 1, 30);
    const progressPercent = ((completedCount / 30) * 100).toFixed(0);

    // Update Hero Stats
    const currentDayEl = document.getElementById('dash-current-day');
    if (currentDayEl) currentDayEl.textContent = `Day ${String(currentDay).padStart(2, '0')} / 30`;

    const progressPctEl = document.getElementById('dash-progress-percent');
    if (progressPctEl) progressPctEl.textContent = `${progressPercent}% Completed`;

    const progressBar = document.getElementById('dash-progress-bar');
    if (progressBar) progressBar.style.width = `${progressPercent}%`;

    // Update Global Stats Row
    const statComp = document.getElementById('stat-completed-exercises');
    if (statComp) statComp.textContent = `${completedCount} / 30`;

    const statSolved = document.getElementById('stat-solved-questions');
    if (statSolved) statSolved.textContent = `${totalQuestionsSolved} / 450`;

    const statAcc = document.getElementById('stat-overall-accuracy');
    if (statAcc) statAcc.textContent = `${overallAccuracy}%`;

    const statAvg = document.getElementById('stat-avg-time');
    if (statAvg) statAvg.textContent = avgTimeSecs !== '--' ? `${avgTimeSecs}s` : '-- s';

    const statTotalTime = document.getElementById('stat-total-practice');
    if (statTotalTime) statTotalTime.textContent = formatDuration(totalTimeSecs);

    // Render 30 Exercise Cards
    renderExerciseCards();
  }

  function renderExerciseCards() {
    const grid = document.getElementById('exercises-cards-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const completedIds = Object.keys(state.completedMap).map(Number);
    const highestCompleted = completedIds.length > 0 ? Math.max(...completedIds) : 0;

    EXERCISES_DATA.forEach(ex => {
      // Filter check (all or range e.g. 1-5, 6-10 or tier name)
      if (state.tierFilter !== 'all') {
        const parts = state.tierFilter.split('-');
        if (parts.length === 2) {
          const start = parseInt(parts[0], 10);
          const end = parseInt(parts[1], 10);
          if (ex.id < start || ex.id > end) return;
        } else if (ex.tier !== state.tierFilter) {
          return;
        }
      }

      const isCompleted = !!state.completedMap[ex.id];
      const isUnlocked = state.settings.unlockAll || ex.id === 1 || ex.id <= highestCompleted + 1;
      const isNextToSolve = !isCompleted && isUnlocked;
      const compData = state.completedMap[ex.id];

      const card = document.createElement('div');
      card.className = `exercise-card ${!isUnlocked ? 'locked' : ''} ${isCompleted ? 'completed' : ''}`;

      // Format Tier Badge
      let tierClass = 'Foundation';
      if (ex.tier.includes('Basic')) tierClass = 'Basic';
      else if (ex.tier === 'Intermediate') tierClass = 'Intermediate';
      else if (ex.tier.includes('Intermediate →')) tierClass = 'Upper-Int';
      else if (ex.tier === 'Advanced') tierClass = 'Advanced';
      else if (ex.tier.includes('Exam')) tierClass = 'Exam-Level';

      let statusHtml = '';
      if (isCompleted) {
        statusHtml = `
          <div class="ex-card-stats">
            <div class="ex-stat-item">
              <span>Score</span>
              <span style="color: var(--success);">${compData.score} / 15</span>
            </div>
            <div class="ex-stat-item">
              <span>Accuracy</span>
              <span>${compData.accuracy}%</span>
            </div>
            <div class="ex-stat-item">
              <span>Time</span>
              <span>${formatTimeMMSS(compData.totalTimeSecs)}</span>
            </div>
          </div>
          <button class="btn btn-secondary btn-sm ex-card-btn" onclick="App.startExercise(${ex.id})">
            🔄 Review / Retake
          </button>
        `;
      } else if (isNextToSolve) {
        statusHtml = `
          <div class="ex-card-stats">
            <div class="ex-stat-item">
              <span>Questions</span>
              <span>15 (5 Sec)</span>
            </div>
            <div class="ex-stat-item">
              <span>Target</span>
              <span>~${ex.estimatedMinutes || 15}m</span>
            </div>
            <div class="ex-stat-item">
              <span>Status</span>
              <span style="color: var(--accent-primary);">▶ Ready</span>
            </div>
          </div>
          <button class="btn btn-primary btn-sm ex-card-btn" onclick="App.startExercise(${ex.id})">
            ▶ Start Day ${String(ex.id).padStart(2, '0')}
          </button>
        `;
      } else {
        statusHtml = `
          <div class="ex-card-stats">
            <div class="ex-stat-item">
              <span>Status</span>
              <span style="color: var(--text-muted);">🔒 Locked</span>
            </div>
            <div class="ex-stat-item">
              <span>Requirement</span>
              <span>Complete Day ${ex.id - 1}</span>
            </div>
          </div>
          <button class="btn btn-secondary btn-sm ex-card-btn" disabled>
            🔒 Complete Previous
          </button>
        `;
      }

      const cleanTitle = ex.title.replace(/^Day \d+:\s*/, '');
      const subtitleText = ex.subtitle || '5 Sections: Mental • Fractions • Powers • Algebra • Scientific';

      card.innerHTML = `
        <div>
          <div class="ex-card-top">
            <span class="ex-id-pill">Day ${String(ex.id).padStart(2, '0')}</span>
            <span class="tier-badge ${tierClass}">${ex.tier}</span>
          </div>
          <h4 class="ex-card-title">${cleanTitle}</h4>
          <p class="ex-card-sub">${subtitleText}</p>
        </div>
        ${statusHtml}
      `;

      grid.appendChild(card);
    });
  }

  function checkResumeBanner() {
    const banner = document.getElementById('resume-banner');
    if (!banner) return;

    if (state.sessionData && state.sessionData.exerciseId) {
      const ex = EXERCISES_DATA.find(e => e.id === state.sessionData.exerciseId);
      if (ex) {
        const answeredCount = Object.keys(state.sessionData.answers || {}).length;
        document.getElementById('resume-title').textContent = `Continue Exercise ${String(ex.id).padStart(2, '0')}`;
        document.getElementById('resume-details').textContent = `${answeredCount} of 15 questions answered`;
        banner.style.display = 'flex';
        return;
      }
    }
    banner.style.display = 'none';
  }

  // ========================================================
  // EXERCISE ARENA CONTROLLER
  // ========================================================
  function startExercise(exerciseId, resume = false) {
    const ex = EXERCISES_DATA.find(e => e.id === exerciseId);
    if (!ex) {
      showToast('Exercise not found');
      return;
    }

    state.activeExercise = ex;

    if (resume && state.sessionData.exerciseId === exerciseId) {
      // Continue from saved session
      state.currentQIndex = findFirstUnansweredIndex();
    } else {
      // Fresh start
      state.currentQIndex = 0;
      state.sessionData = {
        exerciseId: exerciseId,
        answers: {},
        timings: {},
        correctStatus: {},
        totalElapsedSecs: 0,
        isPaused: false
      };
      saveActiveSession();
    }

    // Set Header
    document.getElementById('arena-ex-number').textContent = `Exercise ${String(ex.id).padStart(2, '0')}`;
    document.getElementById('arena-ex-title').textContent = ex.title.split(': ')[1] || ex.title;

    // Start Exercise Master Timer
    startExerciseTimer();

    // Render palette and first question
    renderPalette();
    loadQuestion(state.currentQIndex);

    navigateTo('exercise');
  }

  function findFirstUnansweredIndex() {
    for (let i = 0; i < 15; i++) {
      if (state.sessionData.answers[i] === undefined) {
        return i;
      }
    }
    return 0;
  }

  function renderPalette() {
    const palette = document.getElementById('arena-palette');
    if (!palette) return;
    palette.innerHTML = '';

    for (let i = 0; i < 15; i++) {
      const q = state.activeExercise.questions[i];
      const pill = document.createElement('div');
      pill.className = 'palette-pill';
      pill.textContent = i + 1;

      if (i === state.currentQIndex) pill.classList.add('current');

      if (state.sessionData.answers[i] !== undefined) {
        if (state.sessionData.correctStatus[i]) {
          pill.classList.add('correct');
        } else {
          pill.classList.add('incorrect');
        }
      }

      if (state.bookmarksSet.has(q.id)) {
        pill.classList.add('has-star');
      }

      pill.onclick = () => {
        if (i !== state.currentQIndex) {
          saveCurrentQuestionTiming();
          loadQuestion(i);
        }
      };

      palette.appendChild(pill);
    }
  }

  function loadQuestion(index) {
    state.currentQIndex = index;
    const q = state.activeExercise.questions[index];
    if (!q) return;

    // Update Question Counter & Progress
    const secNum = Math.floor(index / 3) + 1;
    const secQNum = (index % 3) + 1;
    document.getElementById('arena-q-counter').textContent = `Question ${index + 1} of 15 (Sec ${secNum} • Q ${secQNum}/3)`;
    document.getElementById('arena-progress-fill').style.width = `${((index + 1) / 15) * 100}%`;

    // Section Pill
    const secPill = document.getElementById('arena-section-pill');
    secPill.textContent = `Section ${secNum} — ${q.sectionName}`;

    // Arena Day headers
    const exNumEl = document.getElementById('arena-ex-number');
    if (exNumEl) exNumEl.textContent = `Day ${String(state.activeExercise.id).padStart(2, '0')}`;
    const exTitleEl = document.getElementById('arena-ex-title');
    if (exTitleEl) exTitleEl.textContent = state.activeExercise.title.replace(/^Day \d+:\s*/, '');

    // Question Type Label
    document.getElementById('arena-q-type-badge').textContent = q.type === 'mcq' ? 'MCQ (4 Options)' : 'Numeric Calculation';

    // Hint
    const hintBox = document.getElementById('arena-hint-box');
    hintBox.style.display = 'none';
    hintBox.textContent = q.hint || 'Work step-by-step using mental math shortcuts.';

    // Question Math Text
    const qTextEl = document.getElementById('arena-question-text');
    qTextEl.innerHTML = q.question;

    // Unit Addon
    const unitAddon = document.getElementById('arena-unit-addon');
    unitAddon.textContent = q.unit || '';

    // Bookmark status
    updateBookmarkButtonUI(q.id);

    // Form setup based on Question Type
    const formNumeric = document.getElementById('form-numeric');
    const containerMcq = document.getElementById('container-mcq');
    const inputNumeric = document.getElementById('input-numeric-answer');
    const btnSubmitNumeric = document.getElementById('btn-submit-numeric');
    const btnSubmitMcq = document.getElementById('btn-submit-mcq');
    const explanationBox = document.getElementById('arena-explanation-box');

    // Check if question already answered
    const alreadyAnswered = state.sessionData.answers[index] !== undefined;
    const isLastQ = index === 14;

    if (q.type === 'numeric') {
      formNumeric.style.display = 'flex';
      containerMcq.style.display = 'none';
      
      if (alreadyAnswered) {
        inputNumeric.value = state.sessionData.answers[index];
        inputNumeric.disabled = true;
        btnSubmitNumeric.innerHTML = isLastQ ? 'Finish Exercise 🎉 <span class="kbd-hint">↵ Enter</span>' : 'Next Question → <span class="kbd-hint">↵ Enter</span>';
        btnSubmitNumeric.style.display = 'flex';
      } else {
        inputNumeric.value = '';
        inputNumeric.disabled = false;
        btnSubmitNumeric.innerHTML = 'Check Answer <span class="kbd-hint">↵ Enter</span>';
        btnSubmitNumeric.style.display = 'flex';
        // Auto-focus input
        setTimeout(() => inputNumeric.focus(), 30);
      }
    } else {
      // MCQ
      formNumeric.style.display = 'none';
      containerMcq.style.display = 'block';

      renderMcqOptions(q, alreadyAnswered);

      if (alreadyAnswered) {
        btnSubmitMcq.style.display = 'none';
      } else {
        btnSubmitMcq.style.display = 'flex';
        btnSubmitMcq.disabled = true;
      }
    }

    // Explanation Box Handling
    if (alreadyAnswered) {
      showQuestionExplanation(q, index);
      // Pause timer for already answered question
      pauseQuestionTimer();
      // Display previous recorded time
      const recordedTime = state.sessionData.timings[index] || 0;
      document.getElementById('timer-question').textContent = formatSecondsToStopwatch(recordedTime);
    } else {
      explanationBox.style.display = 'none';
      // Start/restart question stopwatch
      startQuestionTimer();
    }

    // Update Palette Pills
    renderPalette();

    // Update Navigation Buttons (Previous / Next / Finish)
    updateArenaNavButtons();

    // Render KaTeX in loaded question
    renderAllMath();
  }

  function renderMcqOptions(q, alreadyAnswered) {
    const grid = document.getElementById('arena-mcq-options');
    grid.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];
    let selectedIndex = state.sessionData.answers[state.currentQIndex];

    q.options.forEach((optText, optIdx) => {
      const card = document.createElement('div');
      card.className = 'mcq-option-card';
      if (selectedIndex === optIdx) {
        card.classList.add('selected');
      }

      card.innerHTML = `
        <span class="option-key-badge">${letters[optIdx]}</span>
        <span class="option-text math-content">${optText}</span>
      `;

      if (!alreadyAnswered) {
        card.onclick = () => {
          document.querySelectorAll('.mcq-option-card').forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          document.getElementById('btn-submit-mcq').disabled = false;
          card.dataset.index = optIdx;
        };
      }

      grid.appendChild(card);
    });
  }

  function updateArenaNavButtons() {
    const btnPrev = document.getElementById('btn-prev-q');
    const btnNext = document.getElementById('btn-next-q');

    btnPrev.disabled = state.currentQIndex === 0;

    const isLastQ = state.currentQIndex === 14;
    const allAnswered = Object.keys(state.sessionData.answers).length === 15;

    if (isLastQ && allAnswered) {
      btnNext.innerHTML = 'Complete Exercise 🎉';
      btnNext.className = 'btn btn-primary btn-submit';
    } else {
      btnNext.innerHTML = 'Next → <span class="kbd-hint">Right Arrow</span>';
      btnNext.className = 'btn btn-primary';
    }
  }

  // ========================================================
  // QUESTION STOPWATCH & EXERCISE TIMERS
  // ========================================================
  function startQuestionTimer() {
    pauseQuestionTimer();
    state.qStartTime = Date.now();
    state.qElapsedCurrentMs = 0;

    const timerEl = document.getElementById('timer-question');
    timerEl.textContent = '00:00';

    state.qTimerInterval = setInterval(() => {
      if (state.sessionData.isPaused) return;
      state.qElapsedCurrentMs = Date.now() - state.qStartTime;
      const totalSecs = state.qElapsedCurrentMs / 1000;
      timerEl.textContent = formatSecondsToStopwatch(totalSecs);
    }, 100);
  }

  function pauseQuestionTimer() {
    if (state.qTimerInterval) {
      clearInterval(state.qTimerInterval);
      state.qTimerInterval = null;
    }
  }

  function saveCurrentQuestionTiming() {
    if (state.sessionData.answers[state.currentQIndex] === undefined) {
      // Question not submitted yet, record in-progress time
      const currentSecs = (state.sessionData.timings[state.currentQIndex] || 0) + (state.qElapsedCurrentMs / 1000);
      state.sessionData.timings[state.currentQIndex] = parseFloat(currentSecs.toFixed(1));
    }
    pauseQuestionTimer();
  }

  function startExerciseTimer() {
    if (state.exTimerInterval) clearInterval(state.exTimerInterval);
    state.exStartTime = Date.now();
    state.exElapsedBaseSecs = state.sessionData.totalElapsedSecs || 0;

    const exTimerEl = document.getElementById('timer-exercise');

    state.exTimerInterval = setInterval(() => {
      if (state.sessionData.isPaused) return;
      const runningSecs = Math.floor((Date.now() - state.exStartTime) / 1000);
      state.sessionData.totalElapsedSecs = state.exElapsedBaseSecs + runningSecs;
      if (exTimerEl) {
        exTimerEl.textContent = formatTimeMMSS(state.sessionData.totalElapsedSecs);
      }
    }, 1000);
  }

  function stopExerciseTimer() {
    if (state.exTimerInterval) {
      clearInterval(state.exTimerInterval);
      state.exTimerInterval = null;
    }
  }

  // ========================================================
  // PAUSE SYSTEM
  // ========================================================
  function togglePause() {
    if (state.currentView !== 'exercise') return;

    state.sessionData.isPaused = !state.sessionData.isPaused;
    const modal = document.getElementById('modal-pause');

    if (state.sessionData.isPaused) {
      pauseQuestionTimer();
      const currentSecs = (state.qElapsedCurrentMs / 1000).toFixed(1);
      document.getElementById('pause-frozen-time').textContent = `${currentSecs}s`;
      modal.style.display = 'flex';
    } else {
      modal.style.display = 'none';
      if (state.sessionData.answers[state.currentQIndex] === undefined) {
        // Resume stopwatch with adjusted start time
        state.qStartTime = Date.now() - state.qElapsedCurrentMs;
        const timerEl = document.getElementById('timer-question');
        state.qTimerInterval = setInterval(() => {
          if (state.sessionData.isPaused) return;
          state.qElapsedCurrentMs = Date.now() - state.qStartTime;
          const totalSecs = state.qElapsedCurrentMs / 1000;
          timerEl.textContent = formatSecondsToStopwatch(totalSecs);
        }, 100);
      }
      state.exStartTime = Date.now();
      state.exElapsedBaseSecs = state.sessionData.totalElapsedSecs;
    }
  }

  // ========================================================
  // ANSWER EVALUATION & SUBMISSION
  // ========================================================
  function submitAnswer() {
    const q = state.activeExercise.questions[state.currentQIndex];
    if (!q) return;

    // Check if already answered
    if (state.sessionData.answers[state.currentQIndex] !== undefined) {
      // Already answered, just advance to next question
      goToNextQuestion();
      return;
    }

    let userAnswerRaw = '';
    let isCorrect = false;

    if (q.type === 'numeric') {
      const input = document.getElementById('input-numeric-answer');
      userAnswerRaw = input.value.trim();

      if (!userAnswerRaw) {
        showToast('Please enter an answer before submitting');
        input.focus();
        return;
      }

      isCorrect = evaluateNumericAnswer(userAnswerRaw, q.answer, q.tolerance);
    } else {
      // MCQ
      const selected = document.querySelector('.mcq-option-card.selected');
      if (!selected) {
        showToast('Please choose an option (A, B, C, or D)');
        return;
      }

      const optIdx = parseInt(selected.dataset.index, 10);
      userAnswerRaw = optIdx;
      isCorrect = (optIdx === q.answer);
    }

    // Stop and record stopwatch time
    pauseQuestionTimer();
    const timeTaken = parseFloat(Math.max((state.qElapsedCurrentMs / 1000), 0.5).toFixed(1));

    // Save in sessionData
    state.sessionData.answers[state.currentQIndex] = userAnswerRaw;
    state.sessionData.timings[state.currentQIndex] = timeTaken;
    state.sessionData.correctStatus[state.currentQIndex] = isCorrect;

    // Save mistake if incorrect
    if (!isCorrect) {
      recordMistake(q, userAnswerRaw);
    }

    // Save persistent active session
    saveActiveSession();

    // Show immediate feedback & explanation
    showQuestionExplanation(q, state.currentQIndex);

    // Disable input and transform button to Next Question
    if (q.type === 'numeric') {
      document.getElementById('input-numeric-answer').disabled = true;
      const isLastQ = state.currentQIndex === 14;
      const btnSubmit = document.getElementById('btn-submit-numeric');
      btnSubmit.innerHTML = isLastQ ? 'Finish Exercise 🎉 <span class="kbd-hint">↵ Enter</span>' : 'Next Question → <span class="kbd-hint">↵ Enter</span>';
      btnSubmit.style.display = 'flex';
    } else {
      document.getElementById('btn-submit-mcq').style.display = 'none';
    }

    // Update Palette & Nav
    renderPalette();
    updateArenaNavButtons();

    // Sound / Haptic if available
    if (window.navigator && window.navigator.vibrate) {
      window.navigator.vibrate(isCorrect ? 30 : [50, 50, 50]);
    }
  }

  // Robust Numeric Evaluator
  function evaluateNumericAnswer(userStr, targetNum, tolerance) {
    if (userStr === '' || userStr === null || userStr === undefined) return false;
    
    // Normalize string
    let str = String(userStr).trim().toLowerCase();
    
    // Remove comma thousand separators
    str = str.replace(/,/g, '');

    // Remove common trailing units that a student might type: e.g. "m/s", "j", "w", "v", "ev", etc.
    str = str.replace(/(m\/s|m\/s\^2|m\/s²|kg|n\/m|n·m|n|j|w|v|ev|a|hz|mhz|pf|µf|uf|kwh|min|s|°|rad\/s|rad|å|angstrom|cm|mm|kpa|pa|%)*$/i, '').trim();

    // Direct string match check
    if (str === String(targetNum).toLowerCase()) return true;

    // Parse fraction: e.g. "11/8", "3/4"
    if (str.includes('/')) {
      const parts = str.split('/');
      if (parts.length === 2) {
        const num = parseFloat(parts[0]);
        const den = parseFloat(parts[1]);
        if (!isNaN(num) && !isNaN(den) && den !== 0) {
          const val = num / den;
          return checkValueMatch(val, targetNum, tolerance);
        }
      }
    }

    // Parse scientific notation: e.g. "3*10^8", "3x10^8", "3×10^8", "1.6e-19"
    if (str.includes('*10^') || str.includes('x10^') || str.includes('×10^') || str.includes('x10^-') || str.includes('*10^-')) {
      const clean = str.replace('×10^', 'e').replace('x10^', 'e').replace('*10^', 'e');
      const val = parseFloat(clean);
      if (!isNaN(val)) {
        return checkValueMatch(val, targetNum, tolerance);
      }
    }

    // Standard Float parsing
    const val = parseFloat(str);
    if (!isNaN(val)) {
      return checkValueMatch(val, targetNum, tolerance);
    }

    return false;
  }

  function checkValueMatch(userVal, targetVal, tolerance) {
    if (tolerance === 0) {
      return Math.abs(userVal - targetVal) < 1e-5;
    }
    
    // Absolute tolerance match
    if (Math.abs(userVal - targetVal) <= tolerance) {
      return true;
    }

    // Relative tolerance match (allows 2.5% deviation for approximations like pi = 3.14 vs 22/7 or g = 9.8 vs 10)
    const relDiff = Math.abs(userVal - targetVal) / Math.max(Math.abs(targetVal), 1e-9);
    if (relDiff <= 0.025) {
      return true;
    }

    return false;
  }

  function showQuestionExplanation(q, index) {
    const box = document.getElementById('arena-explanation-box');
    const banner = document.getElementById('arena-feedback-banner');
    const isCorrect = state.sessionData.correctStatus[index];
    const userAns = state.sessionData.answers[index];
    const timeTaken = state.sessionData.timings[index] || 0;

    box.style.display = 'block';

    banner.className = `feedback-banner ${isCorrect ? 'correct' : 'incorrect'}`;
    banner.innerHTML = isCorrect 
      ? '✓ Correct! Fast and accurate.' 
      : '✕ Incorrect! Review the calculation shortcut below:';

    // Format User Answer
    let userAnsText = userAns;
    if (q.type === 'mcq') {
      const letters = ['A', 'B', 'C', 'D'];
      userAnsText = `${letters[userAns]}: ${q.options[userAns] || ''}`;
    }

    // Format Correct Answer
    let correctAnsText = q.displayAnswer;
    if (q.type === 'mcq') {
      const letters = ['A', 'B', 'C', 'D'];
      correctAnsText = `${letters[q.answer]}: ${q.options[q.answer]}`;
    }

    document.getElementById('arena-sol-user-ans').textContent = userAnsText;
    document.getElementById('arena-sol-correct-ans').textContent = correctAnsText;
    document.getElementById('arena-sol-time').textContent = `${timeTaken}s`;
    document.getElementById('arena-sol-explanation').innerHTML = q.explanation;

    renderAllMath();
  }

  function retryQuestion() {
    const q = state.activeExercise.questions[state.currentQIndex];
    if (!q) return;

    delete state.sessionData.answers[state.currentQIndex];
    delete state.sessionData.correctStatus[state.currentQIndex];

    loadQuestion(state.currentQIndex);
    showToast('Question reset. Timer restarted.');
  }

  function recordMistake(q, userAns) {
    // Add to mistakes list if not already present
    const existingIdx = state.mistakesList.findIndex(m => m.qid === q.id);
    const letters = ['A', 'B', 'C', 'D'];
    const userDisplay = q.type === 'mcq' ? `${letters[userAns]}: ${q.options[userAns]}` : String(userAns);
    const correctDisplay = q.type === 'mcq' ? `${letters[q.answer]}: ${q.options[q.answer]}` : q.displayAnswer;

    const mistakeItem = {
      qid: q.id,
      exerciseId: state.activeExercise.id,
      exerciseTitle: state.activeExercise.title,
      section: q.section,
      sectionName: q.sectionName,
      question: q.question,
      userAnswer: userDisplay,
      correctAnswer: correctDisplay,
      explanation: q.explanation,
      resolved: false,
      timestamp: Date.now()
    };

    if (existingIdx >= 0) {
      state.mistakesList[existingIdx] = mistakeItem;
    } else {
      state.mistakesList.push(mistakeItem);
    }

    saveMistakes();
  }

  // ========================================================
  // QUESTION NAVIGATION
  // ========================================================
  function goToPrevQuestion() {
    if (state.currentQIndex > 0) {
      saveCurrentQuestionTiming();
      loadQuestion(state.currentQIndex - 1);
    }
  }

  function goToNextQuestion() {
    if (state.currentQIndex < 14) {
      saveCurrentQuestionTiming();
      loadQuestion(state.currentQIndex + 1);
    } else {
      // At last question (14)
      const allAnswered = Object.keys(state.sessionData.answers).length === 15;
      if (allAnswered) {
        finishExercise();
      } else {
        const nextUnanswered = findFirstUnansweredIndex();
        showToast(`Navigating to unanswered Question ${nextUnanswered + 1}`);
        saveCurrentQuestionTiming();
        loadQuestion(nextUnanswered);
      }
    }
  }

  // ========================================================
  // BOOKMARK SYSTEM
  // ========================================================
  function toggleCurrentBookmark() {
    if (!state.activeExercise) return;
    const q = state.activeExercise.questions[state.currentQIndex];
    if (!q) return;

    if (state.bookmarksSet.has(q.id)) {
      state.bookmarksSet.delete(q.id);
      showToast('Removed bookmark');
    } else {
      state.bookmarksSet.add(q.id);
      showToast('★ Bookmarked question for revision!');
    }

    saveBookmarks();
    updateBookmarkButtonUI(q.id);
    renderPalette();
  }

  function updateBookmarkButtonUI(qid) {
    const btn = document.getElementById('btn-arena-bookmark');
    const icon = document.getElementById('arena-star-icon');
    const label = document.getElementById('arena-bookmark-label');
    const isBookmarked = state.bookmarksSet.has(qid);

    if (btn) {
      btn.classList.toggle('bookmarked', isBookmarked);
      if (icon) icon.textContent = isBookmarked ? '★' : '☆';
      if (label) label.textContent = isBookmarked ? 'Bookmarked' : 'Bookmark';
    }
  }

  // ========================================================
  // EXERCISE COMPLETION & RESULTS
  // ========================================================
  function finishExercise() {
    stopExerciseTimer();
    pauseQuestionTimer();

    const ex = state.activeExercise;
    const answers = state.sessionData.answers;
    const timings = state.sessionData.timings;
    const correctStatus = state.sessionData.correctStatus;

    let score = 0;
    let secScores = {
      mental: 0,
      fractions: 0,
      powers: 0,
      algebra: 0,
      scientific: 0
    };

    let fastestQ = { index: 0, time: 9999 };
    let slowestQ = { index: 0, time: -1 };
    let incorrectQuestions = [];
    let bookmarkedInExercise = [];

    ex.questions.forEach((q, idx) => {
      const isCorrect = !!correctStatus[idx];
      const time = timings[idx] || 0;

      if (isCorrect) {
        score++;
        if (secScores[q.section] !== undefined) {
          secScores[q.section]++;
        }
      } else {
        incorrectQuestions.push({ q, index: idx, userAns: answers[idx], time });
      }

      if (time < fastestQ.time) fastestQ = { index: idx, time };
      if (time > slowestQ.time) slowestQ = { index: idx, time };

      if (state.bookmarksSet.has(q.id)) {
        bookmarkedInExercise.push({ q, index: idx, isCorrect, time });
      }
    });

    const accuracy = ((score / 15) * 100).toFixed(1);
    const totalTimeSecs = state.sessionData.totalElapsedSecs || 1;
    const avgTimePerQ = (totalTimeSecs / 15).toFixed(1);

    // Save completion record
    state.completedMap[ex.id] = {
      exerciseId: ex.id,
      score: score,
      accuracy: accuracy,
      totalTimeSecs: totalTimeSecs,
      avgTimePerQ: avgTimePerQ,
      sectionScores: secScores,
      questionTimings: timings,
      completedAt: new Date().toISOString()
    };

    saveCompletedMap();
    clearActiveSession();

    // Populate Results Screen
    document.getElementById('results-ex-title').textContent = `Day ${String(ex.id).padStart(2, '0')} Complete`;
    document.getElementById('results-ex-date').textContent = `Completed on ${new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}`;
    document.getElementById('results-score').textContent = `${score} / 15`;
    document.getElementById('results-accuracy').textContent = `${accuracy}% Accuracy`;
    document.getElementById('results-total-time').textContent = formatTimeMMSS(totalTimeSecs);
    document.getElementById('results-avg-time').textContent = `${avgTimePerQ}s`;

    // 5 Section Performance (each out of 3)
    const updateSecUI = (secId) => {
      const val = secScores[secId] || 0;
      const scoreEl = document.getElementById(`results-sec-${secId}`);
      const barEl = document.getElementById(`bar-sec-${secId}`);
      if (scoreEl) scoreEl.textContent = `${val} / 3`;
      if (barEl) barEl.style.width = `${(val / 3) * 100}%`;
    };

    updateSecUI('mental');
    updateSecUI('fractions');
    updateSecUI('powers');
    updateSecUI('algebra');
    updateSecUI('scientific');

    // Fastest / Slowest Highlights
    document.getElementById('results-fastest-q').textContent = `Question ${fastestQ.index + 1} (${fastestQ.time}s)`;
    document.getElementById('results-slowest-q').textContent = `Question ${slowestQ.index + 1} (${slowestQ.time}s)`;

    // Mistakes Panel
    const mistakesPanel = document.getElementById('results-mistakes-panel');
    const mistakesListEl = document.getElementById('results-mistakes-list');
    document.getElementById('results-mistakes-count').textContent = incorrectQuestions.length;

    if (incorrectQuestions.length > 0) {
      mistakesPanel.style.display = 'block';
      mistakesListEl.innerHTML = '';
      incorrectQuestions.forEach(item => {
        const row = document.createElement('div');
        row.className = 'review-item';
        row.innerHTML = `
          <strong>Question ${item.index + 1} (${item.q.sectionName}):</strong>
          <div class="math-content">${item.q.question}</div>
          <div style="font-size: 0.8rem; margin-top: 0.25rem;">
            <span style="color: var(--error);">Your answer: ${item.userAns || 'None'}</span> &bull; 
            <span style="color: var(--success);">Correct: ${item.q.displayAnswer}</span>
          </div>
        `;
        mistakesListEl.appendChild(row);
      });
    } else {
      mistakesPanel.style.display = 'none';
    }

    // Bookmarks Panel
    const bookmarksPanel = document.getElementById('results-bookmarks-panel');
    const bookmarksListEl = document.getElementById('results-bookmarks-list');
    document.getElementById('results-bookmarks-count').textContent = bookmarkedInExercise.length;

    if (bookmarkedInExercise.length > 0) {
      bookmarksPanel.style.display = 'block';
      bookmarksListEl.innerHTML = '';
      bookmarkedInExercise.forEach(item => {
        const row = document.createElement('div');
        row.className = 'review-item';
        row.innerHTML = `
          <strong>★ Question ${item.index + 1} (${item.q.sectionName}):</strong>
          <div class="math-content">${item.q.question}</div>
          <div style="font-size: 0.8rem; margin-top: 0.25rem; color: var(--text-muted);">
            Time: ${item.time}s &bull; Answer: ${item.q.displayAnswer}
          </div>
        `;
        bookmarksListEl.appendChild(row);
      });
    } else {
      bookmarksPanel.style.display = 'none';
    }

    // Start Next Exercise Button
    const nextBtn = document.getElementById('btn-results-next-ex');
    if (ex.id < 30) {
      nextBtn.textContent = `Start Exercise ${String(ex.id + 1).padStart(2, '0')} →`;
      nextBtn.onclick = () => startExercise(ex.id + 1);
      nextBtn.style.display = 'inline-flex';
    } else {
      nextBtn.textContent = '🏆 Complete 30-Day Master!';
      nextBtn.onclick = () => navigateTo('dashboard');
    }

    navigateTo('results');
  }

  // ========================================================
  // PROGRESS GRAPH & ANALYTICS (CANVAS ENGINE)
  // ========================================================
  function renderAnalytics() {
    // Analytics summary metrics
    const completedIds = Object.keys(state.completedMap).map(Number).sort((a, b) => a - b);
    
    if (completedIds.length > 0) {
      let bestScore = 0;
      let fastestTime = 999999;
      let fastestDay = 1;

      completedIds.forEach(id => {
        const rec = state.completedMap[id];
        if (rec.score > bestScore) bestScore = rec.score;
        if (rec.totalTimeSecs < fastestTime) {
          fastestTime = rec.totalTimeSecs;
          fastestDay = id;
        }
      });

      document.getElementById('analytics-best-score').textContent = `${bestScore} / 15`;
      document.getElementById('analytics-fastest-ex').textContent = `${formatTimeMMSS(fastestTime)} (Day ${fastestDay})`;

      if (completedIds.length >= 2) {
        const firstTime = state.completedMap[completedIds[0]].totalTimeSecs;
        const lastTime = state.completedMap[completedIds[completedIds.length - 1]].totalTimeSecs;
        const speedImprovement = (((firstTime - lastTime) / firstTime) * 100).toFixed(0);
        document.getElementById('analytics-time-saved').textContent = `${speedImprovement}%`;
      } else {
        document.getElementById('analytics-time-saved').textContent = '--';
      }
    }

    renderProgressGraph();
  }

  function renderProgressGraph() {
    const canvas = document.getElementById('canvas-progress-chart');
    const emptyOverlay = document.getElementById('empty-chart-overlay');
    if (!canvas) return;

    const completedIds = Object.keys(state.completedMap).map(Number).sort((a, b) => a - b);

    if (completedIds.length === 0) {
      emptyOverlay.style.display = 'flex';
      return;
    } else {
      emptyOverlay.style.display = 'none';
    }

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    const padding = { top: 40, right: 40, bottom: 60, left: 70 };
    const chartWidth = width - padding.left - padding.right;
    const chartHeight = height - padding.top - padding.bottom;

    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const gridColor = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.08)';
    const textColor = isDark ? '#94a3b8' : '#64748b';
    const accentColor = '#3b82f6';

    const metric = state.analyticsMetric;
    const legendEl = document.getElementById('graph-legend');
    legendEl.innerHTML = '';

    // Title setup
    const chartTitle = document.getElementById('graph-title');
    const chartSubtitle = document.getElementById('graph-subtitle');

    if (metric === 'totalTime') {
      chartTitle.textContent = 'Total Exercise Completion Time';
      chartSubtitle.textContent = 'Time in Minutes:Lower is faster';
    } else if (metric === 'avgTime') {
      chartTitle.textContent = 'Average Time per Question';
      chartSubtitle.textContent = 'Time in Seconds';
    } else if (metric === 'accuracy') {
      chartTitle.textContent = 'Accuracy Percentage (%)';
      chartSubtitle.textContent = 'Goal: Consistently above 90%';
    } else if (metric === 'score') {
      chartTitle.textContent = 'Questions Answered Correctly';
      chartSubtitle.textContent = 'Max: 15 Questions';
    } else if (metric === 'sections') {
      chartTitle.textContent = 'Section-wise Performance Breakdown';
      chartSubtitle.textContent = '5 Sections: Mental • Fractions • Powers • Algebra • Scientific';
    }

    // Determine Y range
    let maxY = 15;
    let minY = 0;
    let yLabels = [];

    if (metric === 'totalTime') {
      const timesInMins = completedIds.map(id => state.completedMap[id].totalTimeSecs / 60);
      maxY = Math.max(Math.ceil(Math.max(...timesInMins) * 1.2), 5);
      yLabels = [0, (maxY * 0.25).toFixed(1), (maxY * 0.5).toFixed(1), (maxY * 0.75).toFixed(1), maxY.toFixed(1) + 'm'];
    } else if (metric === 'avgTime') {
      const avgTimes = completedIds.map(id => parseFloat(state.completedMap[id].avgTimePerQ));
      maxY = Math.max(Math.ceil(Math.max(...avgTimes) * 1.2), 30);
      yLabels = [0, Math.round(maxY * 0.25), Math.round(maxY * 0.5), Math.round(maxY * 0.75), maxY + 's'];
    } else if (metric === 'accuracy') {
      maxY = 100;
      yLabels = ['0%', '25%', '50%', '75%', '100%'];
    } else if (metric === 'score') {
      maxY = 15;
      yLabels = [0, 4, 8, 12, 15];
    } else if (metric === 'sections') {
      maxY = 3;
      yLabels = ['0', '1', '2', '3'];
    }

    // Draw Grid Lines & Y Axis Labels
    ctx.strokeStyle = gridColor;
    ctx.lineWidth = 1;
    ctx.font = '11px "JetBrains Mono", monospace';
    ctx.fillStyle = textColor;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';

    const ySteps = yLabels.length - 1;
    for (let i = 0; i <= ySteps; i++) {
      const y = padding.top + (chartHeight / ySteps) * (ySteps - i);
      ctx.beginPath();
      ctx.moveTo(padding.left, y);
      ctx.lineTo(width - padding.right, y);
      ctx.stroke();

      ctx.fillText(yLabels[i], padding.left - 12, y);
    }

    // X Axis Coordinates (1 to 30)
    function getX(dayNum) {
      return padding.left + ((dayNum - 1) / 29) * chartWidth;
    }

    function getY(val) {
      const clamped = Math.max(minY, Math.min(maxY, val));
      return padding.top + chartHeight - ((clamped - minY) / (maxY - minY)) * chartHeight;
    }

    // Draw X Axis Day Ticks
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (let day = 1; day <= 30; day += (width < 600 ? 5 : 2)) {
      const x = getX(day);
      ctx.fillText(`D${day}`, x, padding.top + chartHeight + 10);
    }

    // Draw Metric Data Points & Curves
    if (metric === 'sections') {
      // 5 Curves: Mental (blue), Fractions (emerald), Powers (amber), Algebra (purple), Scientific (pink)
      drawSeries(ctx, completedIds, id => state.completedMap[id].sectionScores?.mental || 0, '#3b82f6', getX, getY);
      drawSeries(ctx, completedIds, id => state.completedMap[id].sectionScores?.fractions || 0, '#10b981', getX, getY);
      drawSeries(ctx, completedIds, id => state.completedMap[id].sectionScores?.powers || 0, '#f59e0b', getX, getY);
      drawSeries(ctx, completedIds, id => state.completedMap[id].sectionScores?.algebra || 0, '#8b5cf6', getX, getY);
      drawSeries(ctx, completedIds, id => state.completedMap[id].sectionScores?.scientific || 0, '#ec4899', getX, getY);

      legendEl.innerHTML = `
        <div class="legend-item"><span class="legend-color-box" style="background: #3b82f6;"></span> Mental (0-3)</div>
        <div class="legend-item"><span class="legend-color-box" style="background: #10b981;"></span> Fractions (0-3)</div>
        <div class="legend-item"><span class="legend-color-box" style="background: #f59e0b;"></span> Powers (0-3)</div>
        <div class="legend-item"><span class="legend-color-box" style="background: #8b5cf6;"></span> Algebra (0-3)</div>
        <div class="legend-item"><span class="legend-color-box" style="background: #ec4899;"></span> Scientific (0-3)</div>
      `;
    } else {
      let extractor = id => state.completedMap[id].totalTimeSecs / 60;
      let color = '#3b82f6';
      let label = 'Total Time (min)';

      if (metric === 'avgTime') {
        extractor = id => parseFloat(state.completedMap[id].avgTimePerQ);
        color = '#f59e0b';
        label = 'Avg Question Time (s)';
      } else if (metric === 'accuracy') {
        extractor = id => parseFloat(state.completedMap[id].accuracy);
        color = '#10b981';
        label = 'Accuracy %';

        // Draw 90% benchmark reference line
        const refY = getY(90);
        ctx.save();
        ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(padding.left, refY);
        ctx.lineTo(width - padding.right, refY);
        ctx.stroke();
        ctx.fillStyle = '#10b981';
        ctx.fillText('90% Target', width - padding.right - 40, refY - 10);
        ctx.restore();
      } else if (metric === 'score') {
        extractor = id => state.completedMap[id].score;
        color = '#8b5cf6';
        label = 'Questions Correct (out of 15)';
      }

      drawSeries(ctx, completedIds, extractor, color, getX, getY, true);

      legendEl.innerHTML = `
        <div class="legend-item"><span class="legend-color-box" style="background: ${color};"></span> ${label} (${completedIds.length} Days Recorded)</div>
      `;
    }
  }

  function drawSeries(ctx, days, valFn, color, getX, getY, fill = false) {
    if (days.length === 0) return;

    const points = days.map(d => ({ x: getX(d), y: getY(valFn(d)), val: valFn(d) }));

    // Area Fill
    if (fill && points.length > 1) {
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(points[0].x, getY(0));
      points.forEach(p => ctx.lineTo(p.x, p.y));
      ctx.lineTo(points[points.length - 1].x, getY(0));
      ctx.closePath();
      const grad = ctx.createLinearGradient(0, points[0].y, 0, getY(0));
      grad.addColorStop(0, color + '44');
      grad.addColorStop(1, color + '00');
      ctx.fillStyle = grad;
      ctx.fill();
      ctx.restore();
    }

    // Line
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.lineJoin = 'round';
    ctx.beginPath();
    points.forEach((p, idx) => {
      if (idx === 0) ctx.moveTo(p.x, p.y);
      else ctx.lineTo(p.x, p.y);
    });
    ctx.stroke();

    // Data points & tooltip labels
    points.forEach(p => {
      ctx.fillStyle = '#ffffff';
      ctx.strokeStyle = color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Text label above point
      ctx.fillStyle = color;
      ctx.font = 'bold 10px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.fillText(typeof p.val === 'number' && !Number.isInteger(p.val) ? p.val.toFixed(1) : p.val, p.x, p.y - 10);
    });
  }

  // ========================================================
  // MISTAKES REVIEW CONTROLLER
  // ========================================================
  function renderMistakesView() {
    const listEl = document.getElementById('mistakes-cards-list');
    if (!listEl) return;
    listEl.innerHTML = '';

    const filter = state.mistakesFilter;
    const items = state.mistakesList.filter(m => {
      if (filter === 'all') return true;
      return m.section === filter;
    });

    // Update counts
    const setSafeCount = (id, count) => {
      const el = document.getElementById(id);
      if (el) el.textContent = count;
    };
    setSafeCount('count-mistakes-all', state.mistakesList.length);
    setSafeCount('count-mistakes-mental', state.mistakesList.filter(m => m.section === 'mental').length);
    setSafeCount('count-mistakes-fractions', state.mistakesList.filter(m => m.section === 'fractions').length);
    setSafeCount('count-mistakes-powers', state.mistakesList.filter(m => m.section === 'powers').length);
    setSafeCount('count-mistakes-algebra', state.mistakesList.filter(m => m.section === 'algebra').length);
    setSafeCount('count-mistakes-scientific', state.mistakesList.filter(m => m.section === 'scientific').length);

    if (items.length === 0) {
      listEl.innerHTML = `
        <div class="empty-state-box">
          <div class="empty-state-icon">🎯</div>
          <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.4rem;">Zero Mistakes Found</h3>
          <p class="empty-state-text">You have no uncorrected mistakes in this category. Keep solving exercises!</p>
          <button class="btn btn-primary btn-sm" onclick="App.navigateTo('dashboard')">Go to Dashboard</button>
        </div>
      `;
      return;
    }

    items.forEach((m, idx) => {
      const card = document.createElement('div');
      card.className = 'mistake-card';
      card.id = `mistake-card-${m.qid}`;

      card.innerHTML = `
        <div class="card-meta-bar">
          <div class="meta-tags">
            <span class="tag-ex">Day ${String(m.exerciseId).padStart(2, '0')}</span>
            <span class="tag-sec">${m.sectionName}</span>
            ${m.resolved ? '<span class="tag-sec" style="color: var(--success); background: var(--success-bg);">✓ Resolved</span>' : ''}
          </div>
          <span class="tag-time">${new Date(m.timestamp).toLocaleDateString()}</span>
        </div>

        <div class="card-question-text math-content">${m.question}</div>

        <div class="mistake-answers-row">
          <div class="ans-block">
            <span class="ans-label">Your Previous Answer:</span>
            <span class="ans-val" style="color: var(--error);">${m.userAnswer}</span>
          </div>
          <div class="ans-block">
            <span class="ans-label">Correct Solution:</span>
            <span class="ans-val" style="color: var(--success);">${m.correctAnswer}</span>
          </div>
        </div>

        <div class="step-by-step-box">
          <div class="step-header">⚡ Method & Shortcut:</div>
          <div class="step-content math-content">${m.explanation}</div>
        </div>

        <div class="mistake-retry-box" id="retry-box-${m.qid}">
          <input type="text" class="mistake-input" id="input-retry-${m.qid}" placeholder="Try solving again..." autocomplete="off">
          <button class="btn btn-secondary btn-sm" onclick="App.checkMistakeRetry('${m.qid}')">Check Solution</button>
        </div>
      `;

      listEl.appendChild(card);
    });

    renderAllMath();
  }

  function checkMistakeRetry(qid) {
    const input = document.getElementById(`input-retry-${qid}`);
    if (!input) return;

    const userVal = input.value.trim();
    if (!userVal) {
      showToast('Enter your retry answer');
      return;
    }

    const exId = parseInt(qid.split('-')[0].replace('ex', ''), 10);
    const ex = EXERCISES_DATA.find(e => e.id === exId);
    if (!ex) return;

    const q = ex.questions.find(item => item.id === qid);
    if (!q) return;

    let isCorrect = false;
    if (q.type === 'numeric') {
      isCorrect = evaluateNumericAnswer(userVal, q.answer, q.tolerance);
    } else {
      const letters = ['a', 'b', 'c', 'd'];
      const optIdx = letters.indexOf(userVal.toLowerCase());
      isCorrect = (optIdx === q.answer || parseInt(userVal, 10) === q.answer);
    }

    if (isCorrect) {
      showToast('✓ Great job! You resolved this calculation.');
      const m = state.mistakesList.find(item => item.qid === qid);
      if (m) {
        m.resolved = true;
        saveMistakes();
      }
      renderMistakesView();
    } else {
      showToast('✕ Still not quite right. Check the shortcut above and try again!');
      input.focus();
    }
  }

  // ========================================================
  // BOOKMARKS CONTROLLER
  // ========================================================
  function renderBookmarksView() {
    const listEl = document.getElementById('bookmarks-cards-list');
    if (!listEl) return;
    listEl.innerHTML = '';

    const bmarkIds = Array.from(state.bookmarksSet);
    document.getElementById('bookmarks-total-badge').textContent = `${bmarkIds.length} Saved`;

    if (bmarkIds.length === 0) {
      listEl.innerHTML = `
        <div class="empty-state-box">
          <div class="empty-state-icon">★</div>
          <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.4rem;">No Bookmarks Yet</h3>
          <p class="empty-state-text">Click the ☆ Bookmark button on any question during your exercise to save it here for fast revision.</p>
          <button class="btn btn-primary btn-sm" onclick="App.navigateTo('dashboard')">Start Training</button>
        </div>
      `;
      return;
    }

    bmarkIds.forEach(qid => {
      const exId = parseInt(qid.split('-')[0].replace('ex', ''), 10);
      const ex = EXERCISES_DATA.find(e => e.id === exId);
      if (!ex) return;

      const q = ex.questions.find(item => item.id === qid);
      if (!q) return;

      const card = document.createElement('div');
      card.className = 'bookmark-card';

      card.innerHTML = `
        <div class="card-meta-bar">
          <div class="meta-tags">
            <span class="tag-ex">Day ${String(ex.id).padStart(2, '0')}</span>
            <span class="tag-sec">${q.sectionName}</span>
            <span class="tag-time">Answer: ${q.displayAnswer}</span>
          </div>
          <button class="btn-icon" style="color: var(--error);" onclick="App.removeBookmark('${qid}')">Remove ✕</button>
        </div>

        <div class="card-question-text math-content">${q.question}</div>

        <div class="step-by-step-box">
          <div class="step-header">⚡ Shortcut:</div>
          <div class="step-content math-content">${q.explanation}</div>
        </div>

        <div style="display: flex; justify-content: flex-end; margin-top: 0.75rem;">
          <button class="btn btn-secondary btn-sm" onclick="App.jumpToQuestion('${qid}')">
            Jump to Question →
          </button>
        </div>
      `;

      listEl.appendChild(card);
    });

    renderAllMath();
  }

  function removeBookmark(qid) {
    state.bookmarksSet.delete(qid);
    saveBookmarks();
    renderBookmarksView();
    showToast('Removed from bookmarks');
  }

  function jumpToQuestion(qid) {
    const exId = parseInt(qid.split('-')[0].replace('ex', ''), 10);
    const ex = EXERCISES_DATA.find(e => e.id === exId);
    if (!ex) return;

    const qIdx = ex.questions.findIndex(item => item.id === qid);
    if (qIdx === -1) return;

    startExercise(exId);
    loadQuestion(qIdx);
  }

  // ========================================================
  // SETTINGS & RESET
  // ========================================================
  function openSettingsModal() {
    const modal = document.getElementById('modal-settings');
    const toggleUnlock = document.getElementById('toggle-unlock-all');
    if (toggleUnlock) toggleUnlock.checked = !!state.settings.unlockAll;
    if (modal) modal.style.display = 'flex';
  }

  function closeSettingsModal() {
    const modal = document.getElementById('modal-settings');
    if (modal) modal.style.display = 'none';
  }

  function resetAllData() {
    if (confirm('Are you sure you want to reset all 30 days of progress, timings, mistakes, and bookmarks? This action cannot be undone.')) {
      try {
        localStorage.removeItem(STORAGE_KEYS.COMPLETED);
        localStorage.removeItem(STORAGE_KEYS.ACTIVE_EXERCISE);
        localStorage.removeItem(STORAGE_KEYS.BOOKMARKS);
        localStorage.removeItem(STORAGE_KEYS.MISTAKES);
      } catch (e) { console.error(e); }

      state.completedMap = {};
      state.bookmarksSet = new Set();
      state.mistakesList = [];
      clearActiveSession();

      closeSettingsModal();
      showToast('All progress reset successfully');
      renderDashboard();
      updateBadges();
    }
  }

  // ========================================================
  // EVENT LISTENERS & SHORTCUTS
  // ========================================================
  function setupEventListeners() {
    // Brand click -> Dashboard
    const brand = document.getElementById('btn-brand');
    if (brand) brand.onclick = () => navigateTo('dashboard');

    // Nav buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.onclick = () => navigateTo(btn.dataset.view);
    });

    // Theme toggle
    const themeBtn = document.getElementById('btn-theme-toggle');
    if (themeBtn) themeBtn.onclick = toggleTheme;

    // Settings toggle
    const settBtn = document.getElementById('btn-settings-toggle');
    if (settBtn) settBtn.onclick = openSettingsModal;

    const closeSett = document.getElementById('btn-close-settings');
    if (closeSett) closeSett.onclick = closeSettingsModal;

    const themeSettingBtn = document.getElementById('btn-settings-theme');
    if (themeSettingBtn) themeSettingBtn.onclick = toggleTheme;

    const toggleUnlock = document.getElementById('toggle-unlock-all');
    if (toggleUnlock) {
      toggleUnlock.onchange = (e) => {
        state.settings.unlockAll = e.target.checked;
        saveSettings();
        renderDashboard();
        showToast(state.settings.unlockAll ? 'All 30 days unlocked!' : 'Progressive unlock restored');
      };
    }

    const resetBtn = document.getElementById('btn-reset-all-data');
    if (resetBtn) resetBtn.onclick = resetAllData;

    // Resume banner buttons
    const btnResumeContinue = document.getElementById('btn-resume-continue');
    if (btnResumeContinue) {
      btnResumeContinue.onclick = () => {
        if (state.sessionData && state.sessionData.exerciseId) {
          startExercise(state.sessionData.exerciseId, true);
        }
      };
    }

    const btnResumeRestart = document.getElementById('btn-resume-restart');
    if (btnResumeRestart) {
      btnResumeRestart.onclick = () => {
        if (state.sessionData && state.sessionData.exerciseId) {
          startExercise(state.sessionData.exerciseId, false);
        }
      };
    }

    // Tier filter chips in Dashboard
    const filterContainer = document.getElementById('tier-filter-chips');
    if (filterContainer) {
      filterContainer.onclick = (e) => {
        if (e.target.classList.contains('chip')) {
          filterContainer.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
          e.target.classList.add('active');
          state.tierFilter = e.target.dataset.filter;
          renderExerciseCards();
        }
      };
    }

    // Arena Controls
    const btnArenaExit = document.getElementById('btn-arena-exit');
    if (btnArenaExit) btnArenaExit.onclick = () => navigateTo('dashboard');

    const btnArenaPause = document.getElementById('btn-arena-pause');
    if (btnArenaPause) btnArenaPause.onclick = togglePause;

    const btnPauseResume = document.getElementById('btn-pause-resume');
    if (btnPauseResume) btnPauseResume.onclick = togglePause;

    const btnPauseExit = document.getElementById('btn-pause-exit');
    if (btnPauseExit) {
      btnPauseExit.onclick = () => {
        togglePause();
        navigateTo('dashboard');
      };
    }

    const btnArenaBookmark = document.getElementById('btn-arena-bookmark');
    if (btnArenaBookmark) btnArenaBookmark.onclick = toggleCurrentBookmark;

    const btnToggleHint = document.getElementById('btn-toggle-hint');
    if (btnToggleHint) {
      btnToggleHint.onclick = () => {
        const hb = document.getElementById('arena-hint-box');
        hb.style.display = hb.style.display === 'none' ? 'block' : 'none';
      };
    }

    // Submit Numeric Form
    const formNumeric = document.getElementById('form-numeric');
    if (formNumeric) {
      formNumeric.onsubmit = (e) => {
        e.preventDefault();
        submitAnswer();
      };
    }

    // Submit MCQ
    const btnSubmitMcq = document.getElementById('btn-submit-mcq');
    if (btnSubmitMcq) btnSubmitMcq.onclick = submitAnswer;

    // Retry Question Button
    const btnRetry = document.getElementById('btn-retry-question');
    if (btnRetry) btnRetry.onclick = retryQuestion;

    // Nav Arrows
    const btnPrevQ = document.getElementById('btn-prev-q');
    if (btnPrevQ) btnPrevQ.onclick = goToPrevQuestion;

    const btnNextQ = document.getElementById('btn-next-q');
    if (btnNextQ) btnNextQ.onclick = goToNextQuestion;

    // Results view buttons
    const btnResultsDashboard = document.getElementById('btn-results-dashboard');
    if (btnResultsDashboard) btnResultsDashboard.onclick = () => navigateTo('dashboard');

    const btnResultsReviewMistakes = document.getElementById('btn-results-review-mistakes');
    if (btnResultsReviewMistakes) btnResultsReviewMistakes.onclick = () => navigateTo('mistakes');

    // Graph Metric Toggles
    const graphToggles = document.getElementById('graph-metric-toggles');
    if (graphToggles) {
      graphToggles.onclick = (e) => {
        if (e.target.classList.contains('toggle-btn')) {
          graphToggles.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          state.analyticsMetric = e.target.dataset.metric;
          renderProgressGraph();
        }
      };
    }

    // Mistakes Section Filter Chips
    const mistakesChips = document.getElementById('mistakes-filter-pills');
    if (mistakesChips) {
      mistakesChips.onclick = (e) => {
        if (e.target.classList.contains('chip')) {
          mistakesChips.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
          e.target.classList.add('active');
          state.mistakesFilter = e.target.dataset.sec;
          renderMistakesView();
        }
      };
    }
  }

  // Keyboard Shortcuts
  function setupKeyboardShortcuts() {
    window.addEventListener('keydown', (e) => {
      // Ignore if user is typing in settings or mistakes retry input
      const targetTag = e.target.tagName.toLowerCase();
      const isInput = (targetTag === 'input' || targetTag === 'textarea');

      if (state.currentView === 'exercise') {
        // Space -> Pause/Resume
        if (e.code === 'Space' && (!isInput || document.getElementById('modal-pause').style.display === 'flex')) {
          e.preventDefault();
          togglePause();
          return;
        }

        // When paused, only allow space or escape
        if (state.sessionData.isPaused) {
          if (e.key === 'Escape') togglePause();
          return;
        }

        // Enter -> Submit answer or Go to Next
        if (e.key === 'Enter') {
          e.preventDefault();
          if (state.sessionData.answers[state.currentQIndex] !== undefined) {
            goToNextQuestion();
          } else {
            submitAnswer();
          }
          return;
        }

        // Left Arrow -> Previous question
        if (e.key === 'ArrowLeft' && !isInput) {
          goToPrevQuestion();
          return;
        }

        // Right Arrow -> Next question
        if (e.key === 'ArrowRight' && !isInput) {
          goToNextQuestion();
          return;
        }

        // 'B' or 'b' -> Toggle Bookmark
        if ((e.key === 'b' || e.key === 'B') && !isInput) {
          toggleCurrentBookmark();
          return;
        }

        // 'H' or 'h' -> Toggle Hint
        if ((e.key === 'h' || e.key === 'H') && !isInput) {
          const hb = document.getElementById('arena-hint-box');
          if (hb) hb.style.display = hb.style.display === 'none' ? 'block' : 'none';
          return;
        }

        // Escape -> Exit to Dashboard
        if (e.key === 'Escape' && !state.sessionData.isPaused) {
          navigateTo('dashboard');
          return;
        }

        // '1', '2', '3', '4' -> Select MCQ Options
        const q = state.activeExercise?.questions[state.currentQIndex];
        if (q && q.type === 'mcq' && ['1', '2', '3', '4'].includes(e.key) && !isInput) {
          const optIdx = parseInt(e.key, 10) - 1;
          const cards = document.querySelectorAll('.mcq-option-card');
          if (cards[optIdx]) {
            cards[optIdx].click();
          }
          return;
        }
      }
    });
  }

  // ========================================================
  // UTILITIES & FORMATTERS
  // ========================================================
  function formatSecondsToStopwatch(sec) {
    const total = Math.floor(sec);
    const m = Math.floor(total / 60);
    const s = total % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }

  function formatTimeMMSS(sec) {
    if (!sec || isNaN(sec)) return '00:00';
    const total = Math.floor(sec);
    const m = Math.floor(total / 60);
    const s = total % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }

  function formatDuration(sec) {
    if (!sec || isNaN(sec)) return '0m';
    const total = Math.floor(sec);
    const h = Math.floor(total / 3600);
    const m = Math.floor((total % 3600) / 60);
    if (h > 0) return `${h}h ${m}m`;
    return `${m}m`;
  }

  function showToast(msg) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = msg;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(8px)';
      toast.style.transition = 'all 0.25s ease';
      setTimeout(() => toast.remove(), 250);
    }, 2400);
  }

  // Render Math with KaTeX and offline fallback
  function renderAllMath() {
    if (typeof renderMathInElement === 'function') {
      try {
        renderMathInElement(document.body, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });
        return;
      } catch (e) {
        console.warn('KaTeX rendering error:', e);
      }
    }

    // If KaTeX script is still loading asynchronously, retry shortly
    if (!window._katexRetryCount) window._katexRetryCount = 0;
    if (window._katexRetryCount < 4 && typeof renderMathInElement !== 'function') {
      window._katexRetryCount++;
      setTimeout(renderAllMath, 250);
      return;
    }

    // Offline fallback: transform common LaTeX symbols to readable Unicode
    document.querySelectorAll('.math-content').forEach(el => {
      let html = el.innerHTML;
      if (html.includes('\\(') || html.includes('\\[')) {
        html = html
          .replace(/\\times/g, ' × ')
          .replace(/\\div/g, ' ÷ ')
          .replace(/\\pm/g, ' ± ')
          .replace(/\\approx/g, ' ≈ ')
          .replace(/\\implies/g, ' ⟹ ')
          .replace(/\\Delta/g, 'Δ')
          .replace(/\\pi/g, 'π')
          .replace(/\\theta/g, 'θ')
          .replace(/\\lambda/g, 'λ')
          .replace(/\\mu/g, 'µ')
          .replace(/\\omega/g, 'ω')
          .replace(/\\alpha/g, 'α')
          .replace(/\\beta/g, 'β')
          .replace(/\\varepsilon/g, 'ε')
          .replace(/\\Omega/g, 'Ω')
          .replace(/\\AA/g, 'Å')
          .replace(/\\text\{([^}]+)\}/g, '$1')
          .replace(/\\sqrt\{([^}]+)\}/g, '√($1)')
          .replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '($1/$2)')
          .replace(/\\([()[\]])/g, '');
        el.innerHTML = html;
      }
    });
  }

  // Public Interface for Inline Handlers
  window.App = {
    init,
    navigateTo,
    startExercise,
    checkMistakeRetry,
    removeBookmark,
    jumpToQuestion
  };

  // Start app on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
