# Maths30 — 30-Day Calculation Skill Training Web App

A responsive, client-side calculation training web application designed to systematically rebuild and accelerate mathematics and physics numerical calculation skills for **NEET** and **JEE** aspirants.

![Maths30 Preview](https://img.shields.io/badge/Questions-450%20Curated-blue?style=for-the-badge)
![Curriculum](https://img.shields.io/badge/Curriculum-30%20Days-green?style=for-the-badge)
![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20JS%20(ES6)-orange?style=for-the-badge)
![Offline](https://img.shields.io/badge/Offline-100%25%20Client--Side-purple?style=for-the-badge)

---

## 🌟 Highlights & Features

1. **450 Predefined, High-Yield Questions**
   - Exactly **30 progressive daily exercises**.
   - Exactly **15 questions per exercise** (5 Mental Arithmetic, 5 Algebra, 5 Physics-Style Calculations).
   - **Zero placeholders**: complete dataset built and validated.
   - Real NEET & JEE formulas, physical constants ($h, c, e, \varepsilon_0, \mu_0, G, R, k_B$), and calculation shortcuts ($\pi^2 \approx 10$, $1240\text{ nm}\cdot\text{eV}$, $1/R \approx 91.2\text{ nm}$, $37^\circ/53^\circ$ 3-4-5 triangles).

2. **Difficulty Progression (6 Tiers)**
   - **Exercises 1–5: Foundation** — Arithmetic fundamentals, fractions, decimals, percentage shortcuts, squares ($11^2$–$30^2$), simple formula substitution ($v = s/t, F = ma, W = Fs, P = W/t, V = IR$).
   - **Exercises 6–10: Basic → Intermediate** — Mixed numbers, ratios, proportions, negative integers, difference of squares, $v = u + at$, $s = ut + \frac{1}{2}at^2$, $Q = mc\Delta T$, $E_k = \frac{1}{2}mv^2$, $P = V^2/R$.
   - **Exercises 11–15: Intermediate** — Surds ($\sqrt{2}, \sqrt{3}, \sqrt{5}$), simultaneous equations, unit conversions ($\text{km/h} \leftrightarrow \text{m/s}$, $\text{g/cm}^3 \leftrightarrow \text{kg/m}^3$), fluid pressure ($P = \rho gh$), pendulum periods ($T = 2\pi\sqrt{L/g}$).
   - **Exercises 16–20: Intermediate → Advanced** — Powers of ten ($10^{-19}, 10^{-34}$), NEET standard angles ($30^\circ, 45^\circ, 60^\circ, 37^\circ, 53^\circ$), resolving vectors, universal gravitation, and Coulomb's law.
   - **Exercises 21–25: Advanced** — Capacitance ($C = \varepsilon_0 A/d$), photoelectric effect ($E = h\nu - \Phi$), thermal radiation ($P \propto T^4$), rotational dynamics ($I = \frac{1}{2}MR^2, \frac{2}{5}MR^2$), and time-pressured approximations.
   - **Exercises 26–30: Exam-Level** — Authentic multi-step numericals: Bohr atom transitions ($E_n = -13.6/n^2\text{ eV}$), lens maker formula ($1/f = (\mu-1)(2/R)$), cyclotron frequency ($f = qB/2\pi m$), LCR resonance ($Z = \sqrt{R^2 + (X_L - X_C)^2}$), and radioactive decay half-lives.

3. **Question Stopwatch & Live Timers**
   - Individual live stopwatch for every question ($00:07$).
   - Stops on submit, records exact question time, overall exercise time, and average question speed.
   - When revisiting answered questions, displays previously recorded time and answer.

4. **Pause & Resume System**
   - Dedicated Pause button and `Spacebar` shortcut.
   - Freezes stopwatch and question interaction with a frosted overlay.
   - Seamlessly resumes without losing or inflating recorded time.
   - Full session resumption if leaving midway through an exercise.

5. **Bookmarks & Mistakes Review**
   - **★ Bookmarks**: Star any question for later revision and jump directly to it from the Bookmarks tab.
   - **❌ Mistakes Review**: Dedicated tab listing every incorrectly answered question with previous vs correct answers, step-by-step NEET/JEE shortcut solutions, and an interactive in-place "Try Again" solver.

6. **Interactive Canvas Progress Graph**
   - Plots actual completion time for every finished exercise.
   - Dynamic metric toggles: Total Exercise Time, Average Question Time, Accuracy %, Questions Correct, and Section-Wise Comparison.
   - High-DPI crisp rendering on all screens.

7. **Flexible Answer Input**
   - Primarily numeric entry with robust evaluation: supports integers, decimals (`1.73`), fractions (`11/8`, `3/4`), scientific notation (`3e8`, `1.6*10^-19`, `3×10^8`), and standard unit tolerances.
   - MCQ format for shortcuts and equivalent expressions.

8. **Keyboard Accessibility**
   - `Enter` ➔ Submit answer / Next question
   - `←` (Left Arrow) ➔ Previous question
   - `→` (Right Arrow) ➔ Next question
   - `Space` ➔ Pause / Resume
   - `1`, `2`, `3`, `4` ➔ Select MCQ option A, B, C, D
   - `B` ➔ Toggle Bookmark

---

## 🚀 How to Run

No build tools, package managers, or servers required.

Simply open `index.html` in any web browser:

```bash
# In Linux / macOS:
open index.html
# Or with any local server if desired:
python3 -m http.server 8000
```

---

## 📁 Repository Structure

```
.
├── index.html       # Single-page application shell, semantic views, and modals
├── style.css        # Responsive, modern dark/light styling and KaTeX optimizations
├── questions.js     # Complete database of 30 exercises x 15 questions = 450 questions
├── app.js           # Timers, answer evaluator, localStorage state, and Canvas graphs
├── assemble.py      # Dataset compilation and validation suite
├── data_tier1.py    # Questions for Exercises 1–5 (Foundation)
├── data_tier2.py    # Questions for Exercises 6–10 (Basic → Intermediate)
├── data_tier3.py    # Questions for Exercises 11–15 (Intermediate)
├── data_tier4.py    # Questions for Exercises 16–20 (Intermediate → Advanced)
├── data_tier5.py    # Questions for Exercises 21–25 (Advanced)
├── data_tier6.py    # Questions for Exercises 26–30 (Exam-Level)
└── README.md        # Documentation and curriculum overview
```

---

## 🔒 100% Local Storage Privacy
All progress, scores, bookmarks, mistakes, and preferences are stored exclusively on your device using `window.localStorage`.
