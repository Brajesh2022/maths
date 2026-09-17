# Days 21 - 30: Advanced to High-Speed Exam Level Pure Mathematics Calculations
from math_days_1_10 import q

days_21_30 = []

# Day 21
days_21_30.append({
    "id": 21, "title": "Day 21: High-Power Ratios & Constant Multiplications", "difficulty": 5, "tier": "Advanced",
    "questions": [
        q("ex21-q1", 21, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( \\frac{2}{5} \\times 2.5 \\)", 1, "1", 0, None, "0.4 * 2.5 = 1.", "\\(1\\)."),
        q("ex21-q2", 21, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 12^2 \\div 36 \\)", 4, "4", 0, None, "144 / 36 = 4.", "\\(4\\)."),
        q("ex21-q3", 21, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 0.5 \\times 4 \\times 15^2 \\)", 450, "450", 0, None, "2 * 225 = 450.", "\\(450\\)."),

        q("ex21-q4", 21, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 2\\pi \\times 50 \\). (Use \\( \\pi \\approx 3.14 \\))", 314, "314", 1, None, "100 * 3.14 = 314.", "\\(314\\)."),
        q("ex21-q5", 21, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{2}{5} \\times 5 \\times 0.04 \\)", 0.08, "0.08", 0.005, None, "2 * 0.04 = 0.08.", "\\(0.08\\)."),
        q("ex21-q6", 21, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( 0.5 \\times 0.4 \\times 100 \\)", 20, "20", 0, None, "0.2 * 100 = 20.", "\\(20\\)."),

        q("ex21-q7", 21, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 2^4 \\)", 16, "16", 0, None, "16.", "\\(16\\)."),
        q("ex21-q8", 21, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\left(\\frac{4}{3}\\right)^4 \\). Enter as decimal to 2 places.", 3.16, "3.16 (or 256/81)", 0.05, None, "256 / 81 ≈ 3.16.", "\\(3.16\\)."),
        q("ex21-q9", 21, "powers", "Powers, Roots & Surds", "numeric", "Solve for positive \\( \\omega \\): \\( \\frac{1}{2}(0.5)\\omega^2 = 16 \\)", 8, "8", 0, None, "omega^2 = 64 => omega = 8.", "\\(8\\)."),

        q("ex21-q10", 21, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\frac{12}{3} \\)", 4, "4", 0, None, "4.", "\\(4\\)."),
        q("ex21-q11", 21, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 4 \\times 5 \\)", 20, "20", 0, None, "20.", "\\(20\\)."),
        q("ex21-q12", 21, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 0.5 \\times 4 \\times 25 \\)", 50, "50", 0, None, "2 * 25 = 50.", "\\(50\\)."),

        q("ex21-q13", 21, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{2.9 \\times 10^{-3}}{5800} \\times 10^9 \\)", 500, "500", 5, None, "0.5 * 10^-6 * 10^9 = 500.", "\\(500\\)."),
        q("ex21-q14", 21, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 8.314 \\times 300 \\) to nearest integer.", 2494, "2494", 5, None, "24.942 * 100 = 2494.2.", "\\(2494\\)."),
        q("ex21-q15", 21, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10\\pi \\times 300}{30} \\) with \\( \\pi \\approx 3.1416 \\) to 1 decimal place.", 31.4, "31.4 (or 10π)", 0.5, None, "10 * 3.1416 = 31.42.", "\\(31.4\\).")
    ]
})

# Day 22
days_21_30.append({
    "id": 22, "title": "Day 22: Exponential Powers & Fractional Exponents", "difficulty": 5, "tier": "Advanced",
    "questions": [
        q("ex22-q1", 22, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 1 - \\frac{300}{500} \\). Enter as decimal.", 0.4, "0.4", 0.01, None, "1 - 0.6 = 0.4.", "\\(0.4\\)."),
        q("ex22-q2", 22, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 0.4 \\times 1000 \\)", 400, "400", 0, None, "400.", "\\(400\\)."),
        q("ex22-q3", 22, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 1000 - 400 \\)", 600, "600", 0, None, "600.", "\\(600\\)."),

        q("ex22-q4", 22, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( 8^{2/3} \\)", 4, "4", 0, None, "2^2 = 4.", "\\(4\\)."),
        q("ex22-q5", 22, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 300 \\times 4 \\)", 1200, "1200", 0, None, "1200.", "\\(1200\\)."),
        q("ex22-q6", 22, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{4}{50} \\). Enter as decimal.", 0.08, "0.08", 0.005, None, "8 / 100 = 0.08.", "\\(0.08\\)."),

        q("ex22-q7", 22, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{4} \\)", 2, "2", 0, None, "2.", "\\(2\\)."),
        q("ex22-q8", 22, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 1.5 \\times 2494.2 \\) to nearest integer.", 3741, "3741", 10, None, "3741.3.", "\\(3741\\)."),
        q("ex22-q9", 22, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 0.05 \\times 3.36 \\times 10^5 \\)", 16800, "16,800", 20, None, "0.05 * 336000 = 16800.", "\\(16,800\\)."),

        q("ex22-q10", 22, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\frac{400 \\times 0.01 \\times 50}{0.2} \\)", 1000, "1000", 5, None, "200 / 0.2 = 1000.", "\\(1000\\)."),
        q("ex22-q11", 22, "algebra", "Algebra & Equations", "numeric", "Solve for \\( T \\): \\( 27 + 273 \\)", 300, "300", 0, None, "300.", "\\(300\\)."),
        q("ex22-q12", 22, "algebra", "Algebra & Equations", "numeric", "Solve for \\( T \\): \\( 127 + 273 \\)", 400, "400", 0, None, "400.", "\\(400\\)."),

        q("ex22-q13", 22, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 2.5 \\times 8 \\)", 20, "20", 0, None, "20.", "\\(20\\)."),
        q("ex22-q14", 22, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 0.5 \\times 4 \\times 0.25 \\)", 0.5, "0.5", 0.01, None, "2 * 0.25 = 0.5.", "\\(0.5\\)."),
        q("ex22-q15", 22, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{4900}{100} \\)", 49, "49", 0, None, "49.", "\\(49\\).")
    ]
})

# Day 23: Harmonic Reciprocals & Multi-Factor Simplification
days_21_30.append({
    "id": 23, "title": "Day 23: Harmonic Reciprocals & Multi-Factor Simplification", "difficulty": 5, "tier": "Advanced",
    "questions": [
        q("ex23-q1", 23, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{20} - \\frac{1}{30} \\). Enter the reciprocal of this result.", 60, "60", 0, None, "(3 - 2)/60 = 1/60 => reciprocal is 60.", "\\(60\\)."),
        q("ex23-q2", 23, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{15} + \\frac{1}{30} \\). Enter the reciprocal of this result.", 10, "10", 0, None, "3/30 = 1/10 => reciprocal is 10.", "\\(10\\)."),
        q("ex23-q3", 23, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{15} - \\frac{1}{20} \\). Enter the reciprocal of this result.", 60, "60", 0, None, "(4 - 3)/60 = 1/60 => reciprocal is 60.", "\\(60\\)."),

        q("ex23-q4", 23, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 4 \\div \\frac{4}{3} \\)", 3, "3", 0, None, "4 * 3/4 = 3.", "\\(3\\)."),
        q("ex23-q5", 23, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( (1.5 - 1) \\times 6 \\)", 3, "3", 0, None, "0.5 * 6 = 3.", "\\(3\\)."),
        q("ex23-q6", 23, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{30}{-30} \\)", -1, "-1", 0, None, "-1.", "\\(-1\\)."),

        q("ex23-q7", 23, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{60}{-20} \\)", -3, "-3", 0, None, "-3.", "\\(-3\\)."),
        q("ex23-q8", 23, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 4 \\times 20 \\)", 80, "80", 0, None, "80.", "\\(80\\)."),
        q("ex23-q9", 23, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( \\frac{20}{1} \\times \\frac{25}{5} \\)", 100, "100", 0, None, "20 * 5 = 100.", "\\(100\\)."),

        q("ex23-q10", 23, "algebra", "Algebra & Equations", "numeric", "Solve for \\( f \\): \\( \\frac{1}{f} = (1.5 - 1)\\left(\\frac{2}{20}\\right) \\). Find \\( f \\).", 20, "20", 0.1, None, "1/f = 0.5 * 0.1 = 0.05 => f = 20.", "\\(f = 20\\)."),
        q("ex23-q11", 23, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\frac{100}{5} \\)", 20, "20", 0, None, "20.", "\\(20\\)."),
        q("ex23-q12", 23, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 100 + 5 \\)", 105, "105", 0, None, "105.", "\\(105\\)."),

        q("ex23-q13", 23, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6 \\times 10^{-7} \\times 1}{10^{-3}} \\times 10^3 \\)", 0.6, "0.6", 0.01, None, "6 * 10^-7 * 10^6 = 6 * 10^-1 = 0.6.", "\\(0.6\\)."),
        q("ex23-q14", 23, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{4\\pi \\times 10^{-7} \\times 10}{2\\pi \\times 0.1} \\times 10^5 \\)", 2, "2", 0.01, None, "2 * 10^-5 * 10^5 = 2.", "\\(2\\)."),
        q("ex23-q15", 23, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 1.6 \\times 10^{-19} \\times 3 \\times 10^6 \\times 0.5 \\times 10^{13} \\)", 2.4, "2.4", 0.05, None, "2.4 * 10^-13 * 10^13 = 2.4.", "\\(2.4\\).")
    ]
})

# Day 24: Inverse Powers of Ten & Root Quadratics
days_21_30.append({
    "id": 24, "title": "Day 24: Extreme Powers of Ten Division & Square Roots", "difficulty": 5, "tier": "Advanced",
    "questions": [
        q("ex24-q1", 24, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{\\sqrt{4 \\times 10^{-6} \\times 2.5 \\times 10^{-5}}} \\)", 100000, "100,000 (or 10⁵)", 100, None, "1 / sqrt(10^-10) = 1 / 10^-5 = 100000.", "\\(100,000\\)."),
        q("ex24-q2", 24, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 50 \\times 0.04 \\times 1.5 \\)", 3, "3", 0.01, None, "2 * 1.5 = 3.", "\\(3\\)."),
        q("ex24-q3", 24, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 0.6 \\times 0.5 \\times 4 \\)", 1.2, "1.2", 0.01, None, "0.3 * 4 = 1.2.", "\\(1.2\\)."),

        q("ex24-q4", 24, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( \\frac{4}{0.02} \\times 0.2 \\)", 40, "40", 0.1, None, "200 * 0.2 = 40.", "\\(40\\)."),
        q("ex24-q5", 24, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{400}{2.512} \\) to nearest integer.", 159, "159", 5, None, "159.23.", "\\(159\\)."),
        q("ex24-q6", 24, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 1000 \\times 2 \\times 1.257 \\times 10^{-3} \\) to 2 decimal places.", 2.51, "2.51", 0.05, None, "2.514.", "\\(2.51\\)."),

        q("ex24-q7", 24, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{2 \\times 10^{-7} \\times 10 \\times 20}{0.2} \\times 10^4 \\)", 2, "2", 0.05, None, "2 * 10^-4 * 10^4 = 2.", "\\(2\\)."),
        q("ex24-q8", 24, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{0.002 \\times 50}{10} \\)", 0.01, "0.01", 0.001, None, "0.1 / 10 = 0.01.", "\\(0.01\\)."),
        q("ex24-q9", 24, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{10}{0.002} - 50 \\)", 4950, "4950", 5, None, "5000 - 50 = 4950.", "\\(4950\\)."),

        q("ex24-q10", 24, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\frac{10^8}{6.28} \\times 10^{-6} \\) to 1 decimal place.", 15.9, "15.9", 0.5, None, "100 / 6.28 ≈ 15.92.", "\\(15.9\\)."),
        q("ex24-q11", 24, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 100 \\times 2 \\times 0.05 \\times 0.4 \\times 0.5 \\)", 2, "2", 0.01, None, "10 * 0.2 = 2.", "\\(2\\)."),
        q("ex24-q12", 24, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 9.27 \\times 2 \\)", 18.54, "18.54", 0.1, None, "18.54.", "\\(18.54\\)."),

        q("ex24-q13", 24, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( \\sqrt{40^2 + 30^2} \\)", 50, "50", 0, None, "sqrt(1600 + 900) = 50.", "\\(50\\)."),
        q("ex24-q14", 24, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{40}{50} \\). Enter as decimal.", 0.8, "0.8", 0, None, "0.8.", "\\(0.8\\)."),
        q("ex24-q15", 24, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 220 \\times 1.414 \\) to nearest integer.", 311, "311", 2, None, "311.08.", "\\(311\\).")
    ]
})

# Day 25: Alternating Ratio Formulas & Square Sums
days_21_30.append({
    "id": 25, "title": "Day 25: Radical Equations & Product-to-Sum Fractions", "difficulty": 5, "tier": "Advanced",
    "questions": [
        q("ex25-q1", 25, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 100 \\times 0.7 \\)", 70, "70", 0.1, None, "70.", "\\(70\\)."),
        q("ex25-q2", 25, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{10^{-2}} \\)", 100, "100", 0.1, None, "100.", "\\(100\\)."),
        q("ex25-q3", 25, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{\\sqrt{0.25 \\times 4 \\times 10^{-6}}} \\)", 1000, "1000", 0.1, None, "1 / 10^-3 = 1000.", "\\(1000\\)."),

        q("ex25-q4", 25, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1000}{6.28} \\) to 1 decimal place.", 159.2, "159.2", 1, None, "159.23.", "\\(159.2\\)."),
        q("ex25-q5", 25, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1}{10} \\sqrt{\\frac{0.25}{4 \\times 10^{-6}}} \\)", 25, "25", 0.1, None, "0.1 * 250 = 25.", "\\(25\\)."),
        q("ex25-q6", 25, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 5000 \\times \\frac{220}{2200} \\)", 500, "500", 0, None, "5000 * 0.1 = 500.", "\\(500\\)."),

        q("ex25-q7", 25, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 10 \\times \\frac{220}{2200} \\)", 1, "1", 0, None, "1.", "\\(1\\)."),
        q("ex25-q8", 25, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 220 \\times 5 \\times 0.8 \\)", 880, "880", 1, None, "1100 * 0.8 = 880.", "\\(880\\)."),
        q("ex25-q9", 25, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{100\\pi}{2\\pi} \\)", 50, "50", 0, None, "50.", "\\(50\\)."),

        q("ex25-q10", 25, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\frac{100}{1.414} \\) to 1 decimal place.", 70.7, "70.7", 0.5, None, "70.72.", "\\(70.7\\)."),
        q("ex25-q11", 25, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 10 \\times 0.6 \\)", 6, "6", 0, None, "6.", "\\(6\\)."),
        q("ex25-q12", 25, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 40 \\div 4 \\)", 10, "10", 0, None, "10.", "\\(10\\)."),

        q("ex25-q13", 25, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1.6 \\times 10^{-19} \\times 10^7}{3.2 \\times 10^{-12}} \\)", 0.5, "0.5", 0.01, None, "0.5 * 10^0 = 0.5.", "\\(0.5\\)."),
        q("ex25-q14", 25, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\sqrt{1.44 \\times 10^8} \\)", 12000, "12,000 (or 1.2×10⁴)", 10, None, "1.2 * 10^4 = 12000.", "\\(12,000\\)."),
        q("ex25-q15", 25, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{19.89}{5} \\) to 2 decimal places.", 3.98, "3.98", 0.05, None, "3.978.", "\\(3.98\\).")
    ]
})

# Day 26: Negative Squares & Inverse Squares Series
days_21_30.append({
    "id": 26, "title": "Day 26: Rational Inverse Squares & Series Differences", "difficulty": 5, "tier": "Exam-Level",
    "questions": [
        q("ex26-q1", 26, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( -\\frac{13.6}{1^2} \\)", -13.6, "-13.6", 0.05, None, "-13.6 / 1 = -13.6.", "\\(-13.6\\)."),
        q("ex26-q2", 26, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( -\\frac{13.6}{2^2} \\)", -3.4, "-3.4", 0.05, None, "-13.6 / 4 = -3.4.", "\\(-3.4\\)."),
        q("ex26-q3", 26, "mental", "Mental Arithmetic", "numeric", "Calculate difference: \\( 13.6 - 3.4 \\)", 10.2, "10.2", 0.05, None, "10.2.", "\\(10.2\\)."),

        q("ex26-q4", 26, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( -\\frac{13.6}{3^2} \\) to 2 decimal places.", -1.51, "-1.51", 0.03, None, "-13.6 / 9 ≈ -1.511.", "\\(-1.51\\)."),
        q("ex26-q5", 26, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( -\\frac{13.6}{4^2} \\)", -0.85, "-0.85", 0.02, None, "-13.6 / 16 = -0.85.", "\\(-0.85\\)."),
        q("ex26-q6", 26, "fractions", "Fractions & Decimals", "numeric", "Calculate difference: \\( 3.40 - 1.51 \\)", 1.89, "1.89", 0.02, None, "1.89.", "\\(1.89\\)."),

        q("ex26-q7", 26, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{1240}{10.2} \\) to 1 decimal place.", 121.6, "121.6 (approx 122)", 1.5, None, "1240 / 10.2 ≈ 121.57.", "\\(121.6\\)."),
        q("ex26-q8", 26, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 0.529 \\times 4 \\) to 3 decimal places.", 2.116, "2.116", 0.01, None, "2.116.", "\\(2.116\\)."),
        q("ex26-q9", 26, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{1240}{1.89} \\) to nearest whole number.", 656, "656", 5, None, "1240 / 1.89 ≈ 656.", "\\(656\\)."),

        q("ex26-q10", 26, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\left(\\frac{2}{1}\\right)^3 \\)", 8, "8", 0, None, "2^3 = 8.", "\\(8\\)."),
        q("ex26-q11", 26, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 4 \\times 91.2 \\)", 364.8, "364.8", 1, None, "364.8.", "\\(364.8\\)."),
        q("ex26-q12", 26, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 13.6 \\times 4 \\)", 54.4, "54.4", 0.1, None, "54.4.", "\\(54.4\\)."),

        q("ex26-q13", 26, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1}{1.097 \\times 10^7} \\times 10^9 \\) to 1 decimal place.", 91.2, "91.2", 0.5, None, "100 / 1.097 ≈ 91.15 ≈ 91.2.", "\\(91.2\\)."),
        q("ex26-q14", 26, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{300}{137} \\) to 2 decimal places.", 2.19, "2.19", 0.05, None, "300 / 137 ≈ 2.189.", "\\(2.19\\)."),
        q("ex26-q15", 26, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 1.5 \\times \\frac{80}{60} \\)", 2, "2", 0.01, None, "1.5 * 4/3 = 2.", "\\(2\\).")
    ]
})

# Day 27: Multi-Step Fraction Balancing
days_21_30.append({
    "id": 27, "title": "Day 27: Ratio Scaling & Harmonic Balancing", "difficulty": 5, "tier": "Exam-Level",
    "questions": [
        q("ex27-q1", 27, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 10 \\times \\left(\\frac{75}{60} - 1\\right) \\)", 2.5, "2.5", 0.01, None, "10 * (1.25 - 1) = 10 * 0.25 = 2.5.", "\\(2.5\\)."),
        q("ex27-q2", 27, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 900 \\times \\frac{340}{306} \\)", 1000, "1000", 1, None, "900 * 10/9 = 1000.", "\\(1000\\)."),
        q("ex27-q3", 27, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 10 \\times 4 \\)", 40, "40", 0, None, "40.", "\\(40\\)."),

        q("ex27-q4", 27, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 10 \\times 16 \\)", 160, "160", 0, None, "160.", "\\(160\\)."),
        q("ex27-q5", 27, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( 2 \\times 10^6 \\times 5 \\times 10^{-6} \\)", 10, "10", 0, None, "10.", "\\(10\\)."),
        q("ex27-q6", 27, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 100 \\times 0.632 \\)", 63.2, "63.2", 0.5, None, "63.2.", "\\(63.2\\)."),

        q("ex27-q7", 27, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{0.101}{\\sqrt{100}} \\)", 0.0101, "0.0101", 0.001, None, "0.101 / 10 = 0.0101.", "\\(0.0101\\)."),
        q("ex27-q8", 27, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{3.2 \\times 10^6}{3.2 \\times 10^{-11}} \\times 10^{-17} \\)", 1, "1 (or 10¹⁷ / 10¹⁷)", 0.05, None, "10^17 * 10^-17 = 1.", "\\(1\\)."),
        q("ex27-q9", 27, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{400 \\times 100}{20} \\)", 2000, "2000", 1, None, "20 * 100 = 2000.", "\\(2000\\)."),

        q("ex27-q10", 27, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{x^2 - 64}{x - 8} = 25 \\)", 17, "17", 0, None, "x + 8 = 25 => x = 17.", "\\(x = 17\\)."),
        q("ex27-q11", 27, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( 5x^2 - 125 = 0 \\)", 5, "5", 0, None, "x^2 = 25 => x = 5.", "\\(x = 5\\)."),
        q("ex27-q12", 27, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( x^2 - 15x + 54 = 0 \\). Enter larger root.", 9, "9 (roots are 6, 9)", 0, None, "(x - 6)(x - 9) = 0.", "\\(9\\)."),

        q("ex27-q13", 27, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6.67 \\times 6}{6.4^2} \\) to 2 decimal places.", 0.98, "0.98", 0.05, None, "40.02 / 40.96 ≈ 0.977 ≈ 0.98.", "\\(0.98\\)."),
        q("ex27-q14", 27, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 1.414 \\times 1.732 \\) to 2 decimal places. (\\( \\sqrt{2} \\times \\sqrt{3} = \\sqrt{6} \\))", 2.45, "2.45 (or 2.449)", 0.05, None, "sqrt(6) ≈ 2.449.", "\\(2.45\\)."),
        q("ex27-q15", 27, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 2.236 \\times 2.236 \\) to nearest integer.", 5, "5", 0.1, None, "sqrt(5)^2 = 5.", "\\(5\\).")
    ]
})

# Day 28: Multi-Step Exponent & Logarithm Manipulations
days_21_30.append({
    "id": 28, "title": "Day 28: High-Order Logarithms & Power Products", "difficulty": 5, "tier": "Exam-Level",
    "questions": [
        q("ex28-q1", 28, "mental", "Mental Arithmetic", "numeric", "If \\( \\log_{10}(2) = 0.301 \\) and \\( \\log_{10}(3) = 0.477 \\), find \\( \\log_{10}(6) \\).", 0.778, "0.778", 0.005, None, "0.301 + 0.477 = 0.778.", "\\(0.778\\)."),
        q("ex28-q2", 28, "mental", "Mental Arithmetic", "numeric", "Find \\( \\log_{10}(5) \\). (Recall \\( \\log_{10}(10/2) = 1 - 0.301 \\))", 0.699, "0.699", 0.005, None, "1 - 0.301 = 0.699.", "\\(0.699\\)."),
        q("ex28-q3", 28, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 125 \\times 64 \\)", 8000, "8000", 0, None, "125 * 8 * 8 = 1000 * 8 = 8000.", "\\(8000\\)."),

        q("ex28-q4", 28, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1}{1.25} \\). Enter as decimal.", 0.8, "0.8", 0.01, None, "1 / (5/4) = 4/5 = 0.8.", "\\(0.8\\)."),
        q("ex28-q5", 28, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1}{2.5} \\). Enter as decimal.", 0.4, "0.4", 0.01, None, "1 / (5/2) = 2/5 = 0.4.", "\\(0.4\\)."),
        q("ex28-q6", 28, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1}{0.05} \\)", 20, "20", 0, None, "100 / 5 = 20.", "\\(20\\)."),

        q("ex28-q7", 28, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 3^4 - 2^4 \\)", 65, "65", 0, None, "81 - 16 = 65.", "\\(65\\)."),
        q("ex28-q8", 28, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 4^3 + 5^3 \\)", 189, "189", 0, None, "64 + 125 = 189.", "\\(189\\)."),
        q("ex28-q9", 28, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{0.0004} \\)", 0.02, "0.02", 0.001, None, "0.02 * 0.02 = 0.0004.", "\\(0.02\\)."),

        q("ex28-q10", 28, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 4^{x - 1} = 64 \\)", 4, "4", 0, None, "x - 1 = 3 => x = 4.", "\\(x = 4\\)."),
        q("ex28-q11", 28, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{3x + 4}{2x - 1} = 2 \\)", 6, "6", 0, None, "3x + 4 = 4x - 2 => x = 6.", "\\(x = 6\\)."),
        q("ex28-q12", 28, "algebra", "Algebra & Equations", "numeric", "If \\( x^2 + y^2 = 100 \\) and \\( xy = 48 \\), find \\( x + y \\) (positive value).", 14, "14", 0, None, "(x+y)^2 = 100 + 96 = 196 => 14.", "\\(14\\)."),

        q("ex28-q13", 28, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10^{-12} \\times 10^7}{10^{-8}} \\)", 1000, "1000 (or 10³)", 0.1, None, "-12 + 7 - (-8) = 3 => 10^3.", "\\(1000\\)."),
        q("ex28-q14", 28, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 0.0025 \\times 4000 \\)", 10, "10", 0.01, None, "2.5 * 4 = 10.", "\\(10\\)."),
        q("ex28-q15", 28, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{3.1416 \\times 40}{2} \\) to 1 decimal place.", 62.8, "62.8", 0.5, None, "20 * 3.1416 ≈ 62.83.", "\\(62.8\\).")
    ]
})

# Day 29: Advanced Surd Expansions & High-Precision Fractions
days_21_30.append({
    "id": 29, "title": "Day 29: Surd Conjugates & Nested Square Roots", "difficulty": 5, "tier": "Exam-Level",
    "questions": [
        q("ex29-q1", 29, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( (\\sqrt{5} + \\sqrt{2})(\\sqrt{5} - \\sqrt{2}) \\)", 3, "3", 0, None, "5 - 2 = 3.", "\\(3\\)."),
        q("ex29-q2", 29, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( (\\sqrt{7} + \\sqrt{3})(\\sqrt{7} - \\sqrt{3}) \\)", 4, "4", 0, None, "7 - 3 = 4.", "\\(4\\)."),
        q("ex29-q3", 29, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 2.5 \\times 1.6 \\)", 4, "4", 0.01, None, "5/2 * 8/5 = 4.", "\\(4\\)."),

        q("ex29-q4", 29, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( \\frac{1}{\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6}} \\)", 1, "1", 0, None, "3/6 + 2/6 + 1/6 = 6/6 = 1. Reciprocal is 1.", "\\(1\\)."),
        q("ex29-q5", 29, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 12.5 \\times 0.64 \\)", 8, "8", 0.01, None, "100/8 * 0.64 = 8.", "\\(8\\)."),
        q("ex29-q6", 29, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{0.036}{0.009} \\)", 4, "4", 0, None, "36 / 9 = 4.", "\\(4\\)."),

        q("ex29-q7", 29, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{1000000} \\)", 1000, "1000 (or 10³)", 0, None, "10^3 = 1000.", "\\(1000\\)."),
        q("ex29-q8", 29, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{0.000081} \\)", 0.009, "0.009", 0.0001, None, "9 * 10^-3 = 0.009.", "\\(0.009\\)."),
        q("ex29-q9", 29, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 11^3 \\)", 1331, "1331", 0, None, "121 * 11 = 1331.", "\\(1331\\)."),

        q("ex29-q10", 29, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{x^2 - 100}{x + 10} = 15 \\)", 25, "25", 0, None, "x - 10 = 15 => x = 25.", "\\(x = 25\\)."),
        q("ex29-q11", 29, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( x^2 - 16x + 63 = 0 \\). Enter larger root.", 9, "9 (roots are 7, 9)", 0, None, "(x - 7)(x - 9) = 0.", "\\(9\\)."),
        q("ex29-q12", 29, "algebra", "Algebra & Equations", "numeric", "If \\( a + b = 12 \\) and \\( a - b = 4 \\), find \\( ab \\).", 32, "32", 0, None, "a = 8, b = 4 => 8 * 4 = 32.", "\\(32\\)."),

        q("ex29-q13", 29, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1.6 \\times 10^{-19} \\times 500}{2 \\times 10^{-17}} \\)", 4, "4", 0.05, None, "(1.6 * 500 / 2) * 10^-2 = 400 * 10^-2 = 4.", "\\(4\\)."),
        q("ex29-q14", 29, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 3.1416^2 \\) to 2 decimal places.", 9.87, "9.87 (approx 10)", 0.1, None, "pi^2 ≈ 9.8696.", "\\(9.87\\)."),
        q("ex29-q15", 29, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10^5 - 10^3}{10^3} \\)", 99, "99", 0, None, "100 - 1 = 99.", "\\(99\\).")
    ]
})

# Day 30: Grand Speed Mastery Challenge
days_21_30.append({
    "id": 30, "title": "Day 30: The Grand Finale — High-Speed Calculation Challenge", "difficulty": 5, "tier": "Exam-Level",
    "questions": [
        q("ex30-q1", 30, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 19 \\times 18 \\)", 342, "342", 0, None, "19 * (20 - 2) = 380 - 38 = 342.", "\\(342\\)."),
        q("ex30-q2", 30, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 28 \\times 25 \\)", 700, "700", 0, None, "28 / 4 * 100 = 700.", "\\(700\\)."),
        q("ex30-q3", 30, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 85^2 - 15^2 \\)", 7000, "7000", 0, None, "(85 - 15)(85 + 15) = 70 * 100 = 7000.", "\\(7000\\)."),

        q("ex30-q4", 30, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 37.5\\% \\) of \\( 640 \\)", 240, "240", 0, None, "3/8 * 640 = 3 * 80 = 240.", "\\(240\\)."),
        q("ex30-q5", 30, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1}{0.025} \\)", 40, "40", 0, None, "1000 / 25 = 40.", "\\(40\\)."),
        q("ex30-q6", 30, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 8.5^2 \\)", 72.25, "72.25", 0.01, None, "8 * 9 = 72 => 72.25.", "\\(72.25\\)."),

        q("ex30-q7", 30, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 64^{2/3} \\)", 16, "16", 0, None, "(4)^2 = 16.", "\\(16\\)."),
        q("ex30-q8", 30, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 81^{3/4} \\)", 27, "27", 0, None, "(3)^3 = 27.", "\\(27\\)."),
        q("ex30-q9", 30, "powers", "Powers, Roots & Surds", "numeric", "Simplify: \\( \\sqrt{300} \\div \\sqrt{3} \\)", 10, "10", 0, None, "sqrt(100) = 10.", "\\(10\\)."),

        q("ex30-q10", 30, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( 3x^2 - 48 = 0 \\)", 4, "4", 0, None, "x^2 = 16 => x = 4.", "\\(x = 4\\)."),
        q("ex30-q11", 30, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( x^2 - 17x + 72 = 0 \\). Enter larger root.", 9, "9 (roots are 8, 9)", 0, None, "(x - 8)(x - 9) = 0.", "\\(9\\)."),
        q("ex30-q12", 30, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{5x - 3}{3} = \\frac{3x + 7}{2} \\)", 27, "27", 0, None, "10x - 6 = 9x + 21 => x = 27.", "\\(x = 27\\)."),

        q("ex30-q13", 30, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6.6 \\times 3 \\times 10^{-26}}{4.5 \\times 10^{-19}} \\times 10^7 \\) to 1 decimal place.", 4.4, "4.4", 0.2, None, "(19.8 / 4.5) * 10^(-7) * 10^7 = 4.4.", "\\(4.4\\)."),
        q("ex30-q14", 30, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 125 \\times 0.064 \\)", 8, "8", 0.01, None, "1000/8 * 0.064 = 8.", "\\(8\\)."),
        q("ex30-q15", 30, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{4.8 \\times 10^{-18}}{1.6 \\times 10^{-19}} \\)", 30, "30", 0.01, None, "(4.8 / 1.6) * 10^1 = 3 * 10 = 30.", "\\(30\\).")
    ]
})

print(f"Days 21-30 created: {len(days_21_30)} exercises.")
