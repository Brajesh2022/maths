# Maths30 — 30-Day Math & Calculation Skill Training Web App

A clean, minimalist, responsive client-side calculation training web app designed to systematically rebuild and accelerate basic mathematics and numerical calculation speed for **NEET** and **JEE** aspirants.

![Maths30 Questions](https://img.shields.io/badge/Questions-450%20Curated-blue?style=for-the-badge)
![Curriculum](https://img.shields.io/badge/Curriculum-30%20Days-green?style=for-the-badge)
![Sections](https://img.shields.io/badge/Daily%20Sections-5%20Uniform-orange?style=for-the-badge)
![Offline](https://img.shields.io/badge/Offline-100%25%20Client--Side-purple?style=for-the-badge)

---

## 🎯 Purpose & Philosophy

Physics and Chemistry numericals in NEET & JEE often consume excess time not because of physical formulas, but because of slow raw arithmetic: simplifying fractions, dividing by decimals like $2.5$ or $0.125$, estimating square roots like $\sqrt{2}, \sqrt{3}, \sqrt{10}$, handling powers of ten ($10^{-19}, 10^{-34}$), and solving linear/quadratic equations.

**Maths30 contains zero physics theory or physics formulas.** Instead, it trains raw mathematical reflexes across 30 progressive daily exercises so that numerical calculations in Physics, Chemistry, and Mathematics become second nature.

---

## 🌟 Core Structure (Uniform 5 Sections / Day)

Every single one of the 30 daily exercises consists of the exact same 5 progressive sections:

| # | Section Name | Questions | Calculation Skills Trained |
|---|--------------|-----------|----------------------------|
| 1 | **Mental Arithmetic** | 3 | Multiplication shortcuts, splitting sums, complements to 100/1000, difference of squares |
| 2 | **Fractions & Decimals** | 3 | Decimal reciprocals ($1/0.125 = 8$), percentage splits ($12.5\%, 37.5\%$), multi-term fraction simplification |
| 3 | **Powers, Roots & Surds** | 3 | Squares ($11^2$ to $30^2$), surd values ($\sqrt{2} \approx 1.414, \sqrt{3} \approx 1.732, \sqrt{5} \approx 2.236$), rationalization |
| 4 | **Algebra & Equations** | 3 | Linear equations, cross-multiplication, quadratic factorizations, system balancing |
| 5 | **Scientific Notation & Estimation** | 3 | Powers of ten arithmetic ($10^{-26}/10^{-19}$), $\pi \approx 3.14$, $\pi^2 \approx 10$, ratio scaling |

**Total:** 5 sections × 3 questions = **15 questions per exercise × 30 exercises = 450 questions total.**

---

## ⚡ Minimalist, Low-Click, Keyboard-First UX

- **Zero-Click Hands-On-Keyboard Flow**:
  1. Open a Day. The answer input is **auto-focused** immediately.
  2. Type your answer and press `Enter` to check.
  3. Correct/Incorrect feedback and rapid shortcut explanation appear instantly.
  4. Press `Enter` again to immediately advance to the next question with the input pre-focused and cleared.
- **Stopwatch & Speed Tracking**:
  - Live question stopwatch in monospace font (`00:08`).
  - Total exercise timer and average calculation speed per question.
- **Space to Pause**:
  - Hit `Space` to freeze all timers with a minimalist modal overlay.
- **Bookmarks & Mistakes Review**:
  - Press `B` to star any tricky question for later quick revision.
  - Missed questions are automatically logged to the **Mistakes Review** tab with interactive retry.
- **Interactive HTML5 Canvas Chart**:
  - Track speed improvements across the 30 days: total time, avg time/question, accuracy %, and 5-section comparison.
- **100% Client-Side Privacy**:
  - All progress, times, and bookmarks persist in `localStorage` without any external server or account needed.

---

## 🚀 How to Run

No build tools, npm packages, or backend required. Simply open `index.html` in any modern web browser:

```bash
# In Linux / macOS:
open index.html

# Or with python simple HTTP server:
python3 -m http.server 8000
```

---

## 📁 Repository Structure

```
.
├── index.html              # Minimalist single-page application shell
├── style.css               # Clean dark/light theme, typography, and responsive styles
├── questions.js            # Complete dataset: 30 days x 15 questions = 450 pure-math calculations
├── app.js                  # Timers, answer evaluator, keyboard navigation, and Canvas chart
├── math_days_1_10.py       # Modular question generator for Days 1–10
├── math_days_11_20.py      # Modular question generator for Days 11–20
├── math_days_21_30.py      # Modular question generator for Days 21–30
├── assemble_pure_math.py   # Dataset validator & assembler into questions.js
└── README.md               # Documentation and curriculum guide
```

---

## 🔒 Keyboard Shortcuts Reference

| Key | Action |
|-----|--------|
| `Enter` | Submit answer / Advance to next question |
| `Space` | Pause / Resume exercise timer |
| `B` | Star / Unstar bookmark |
| `H` | Toggle mental shortcut hint |
| `←` / `→` | Previous / Next question |
| `Esc` | Return to Dashboard |
