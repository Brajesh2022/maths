# Days 11 - 20: Intermediate to Upper-Intermediate Pure Mathematics Calculations
from math_days_1_10 import q

days_11_20 = []

# Day 11
days_11_20.append({
    "id": 11, "title": "Day 11: Quadratic Factorization & Squares (28² to 30²)", "difficulty": 3, "tier": "Intermediate",
    "questions": [
        q("ex11-q1", 11, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 84 \\times 15 \\)", 1260, "1260", 0, None, "840 + 420 = 1260.", "\\(840 + 420 = 1260\\)."),
        q("ex11-q2", 11, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{0.04} \\)", 25, "25", 0, None, "100 / 4 = 25.", "\\(100 \\div 4 = 25\\)."),
        q("ex11-q3", 11, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 12.5\\% \\) of \\( 720 \\)", 90, "90", 0, None, "720 / 8 = 90.", "\\(720 \\div 8 = 90\\)."),

        q("ex11-q4", 11, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 6.5^2 \\)", 42.25, "42.25", 0.01, None, "6 * 7 = 42 => 42.25.", "\\(6.5^2 = 42.25\\)."),
        q("ex11-q5", 11, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{6 \\times 3}{6 + 3} \\)", 2, "2", 0.01, None, "Product over sum: 18 / 9 = 2.", "\\(\\frac{18}{9} = 2\\)."),
        q("ex11-q6", 11, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 0.025 \\times 400 \\)", 10, "10", 0.01, None, "2.5 * 4 = 10.", "\\(0.025 \\times 400 = 10\\)."),

        q("ex11-q7", 11, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 28^2 \\)", 784, "784", 0, None, "28 * 28 = 784.", "\\(28^2 = 784\\)."),
        q("ex11-q8", 11, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 29^2 \\)", 841, "841", 0, None, "(30 - 1)^2 = 900 - 60 + 1 = 841.", "\\(29^2 = 841\\)."),
        q("ex11-q9", 11, "powers", "Powers, Roots & Surds", "numeric", "Simplify: \\( \\sqrt{180} \\div \\sqrt{5} \\)", 6, "6", 0, None, "sqrt(180 / 5) = sqrt(36) = 6.", "\\(\\sqrt{36} = 6\\)."),

        q("ex11-q10", 11, "algebra", "Algebra & Equations", "numeric", "Solve the quadratic equation \\( t^2 - 7t + 10 = 0 \\). What is the larger root?", 5, "5 (roots are 2, 5)", 0, None, "(t - 2)(t - 5) = 0.", "\\((t-2)(t-5) = 0\\). Larger root is 5."),
        q("ex11-q11", 11, "algebra", "Algebra & Equations", "numeric", "If \\( x + \\frac{1}{x} = 5 \\), what is \\( x^2 + \\frac{1}{x^2} \\)?", 23, "23", 0, None, "5^2 - 2 = 25 - 2 = 23.", "\\(5^2 - 2 = 23\\)."),
        q("ex11-q12", 11, "algebra", "Algebra & Equations", "numeric", "Solve the system for \\( x \\): \\( 4x + 3y = 25 \\) and \\( x + 2y = 10 \\).", 4, "4", 0, None, "x = 10 - 2y. 4(10 - 2y) + 3y = 25 => 5y = 15 => y = 3 => x = 4.", "\\(x = 4, y = 3\\)."),

        q("ex11-q13", 11, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{4 \\times 10^{-6} \\times 9 \\times 10^9}{3 \\times 10^{-2}} \\)", 1200000, "1,200,000 (or 1.2×10⁶)", 1, None, "12 * 10^5 = 1200000.", "\\(12 \\times 10^5 = 1,200,000\\)."),
        q("ex11-q14", 11, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 1000 \\times 9.8 \\times 10 \\)", 98000, "98,000", 1, None, "9800 * 10 = 98000.", "\\(98,000\\)."),
        q("ex11-q15", 11, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1}{2.5 \\times 10^{-3}} \\)", 400, "400", 0.1, None, "1000 / 2.5 = 400.", "\\(\\frac{1000}{2.5} = 400\\).")
    ]
})

# Day 12
days_11_20.append({
    "id": 12, "title": "Day 12: Algebraic Identities & Radical Fractions", "difficulty": 3, "tier": "Intermediate",
    "questions": [
        q("ex12-q1", 12, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 96 \\times 25 \\)", 2400, "2400", 0, None, "96 / 4 * 100 = 2400.", "\\(24 \\times 100 = 2400\\)."),
        q("ex12-q2", 12, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{0.125} \\)", 8, "8", 0, None, "0.125 = 1/8. Reciprocal is 8.", "\\(1 \\div 0.125 = 8\\)."),
        q("ex12-q3", 12, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 45\\% \\) of \\( 800 \\)", 360, "360", 0, None, "45 * 8 = 360.", "\\(45 \\times 8 = 360\\)."),

        q("ex12-q4", 12, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 7.5^2 \\)", 56.25, "56.25", 0.01, None, "7 * 8 = 56 => 56.25.", "\\(7.5^2 = 56.25\\)."),
        q("ex12-q5", 12, "fractions", "Fractions & Decimals", "numeric", "Simplify \\( \\frac{a^2 - b^2}{a - b} \\) when \\( a = 3.7 \\) and \\( b = 1.3 \\).", 5, "5", 0.01, None, "Reduces to a + b = 3.7 + 1.3 = 5.", "\\(3.7 + 1.3 = 5\\)."),
        q("ex12-q6", 12, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{400 \\times 225}{100} \\)", 900, "900", 0, None, "4 * 225 = 900.", "\\(4 \\times 225 = 900\\)."),

        q("ex12-q7", 12, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 30^2 \\)", 900, "900", 0, None, "30 * 30 = 900.", "\\(30^2 = 900\\)."),
        q("ex12-q8", 12, "powers", "Powers, Roots & Surds", "numeric", "Simplify: \\( \\sqrt{242} \\div \\sqrt{2} \\)", 11, "11", 0, None, "sqrt(121) = 11.", "\\(\\sqrt{121} = 11\\)."),
        q("ex12-q9", 12, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{15^2 + 20^2} \\)", 25, "25", 0, None, "5 * sqrt(3^2 + 4^2) = 5 * 5 = 25.", "\\(\\sqrt{225 + 400} = 25\\)."),

        q("ex12-q10", 12, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{4}{x} - \\frac{1}{2x} = \\frac{7}{12} \\)", 6, "6", 0, None, "7/(2x) = 7/12 => 2x = 12 => x = 6.", "\\(2x = 12 \\implies x = 6\\)."),
        q("ex12-q11", 12, "algebra", "Algebra & Equations", "numeric", "Find the larger root of \\( x^2 - 13x + 36 = 0 \\).", 9, "9 (roots are 4, 9)", 0, None, "(x - 4)(x - 9) = 0.", "\\((x-4)(x-9) = 0\\). Larger root is 9."),
        q("ex12-q12", 12, "algebra", "Algebra & Equations", "numeric", "If \\( x - y = 3 \\) and \\( x^2 - y^2 = 39 \\), what is \\( x + y \\)?", 13, "13", 0, None, "39 / 3 = 13.", "\\(x + y = \\frac{39}{3} = 13\\)."),

        q("ex12-q13", 12, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 2 \\times 10^5 \\times 3 \\times 10^{-3} \\)", 600, "600", 0.1, None, "6 * 10^2 = 600.", "\\(6 \\times 100 = 600\\)."),
        q("ex12-q14", 12, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1}{2\\pi \\times (1/\\pi)} \\)", 0.5, "0.5 (or 1/2)", 0.01, None, "pi cancels: 1/2 = 0.5.", "\\(\\frac{1}{2} = 0.5\\)."),
        q("ex12-q15", 12, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 0.075 \\times 0.4 \\)", 0.03, "0.03", 0.002, None, "75 * 4 = 300. Shift 4 places.", "\\(0.03\\).")
    ]
})

# Day 13: Fractional Exponents
days_11_20.append({
    "id": 13, "title": "Day 13: Fractional Powers & Negative Exponents", "difficulty": 3, "tier": "Intermediate",
    "questions": [
        q("ex13-q1", 13, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 8^{2/3} \\)", 4, "4", 0, None, "(8^(1/3))^2 = 2^2 = 4.", "\\(2^2 = 4\\)."),
        q("ex13-q2", 13, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 16^{-3/4} \\). Enter as decimal.", 0.125, "0.125 (or 1/8)", 0.005, None, "1 / (2^3) = 1/8 = 0.125.", "\\(\\frac{1}{8} = 0.125\\)."),
        q("ex13-q3", 13, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 125 \\times 0.032 \\)", 4, "4", 0.01, None, "125 * 32 = 4000. Shift 3 places.", "\\(4\\)."),

        q("ex13-q4", 13, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( 3.2 \\times 10^{-19} \\div (1.6 \\times 10^{-19}) \\)", 2, "2", 0, None, "Powers cancel: 3.2 / 1.6 = 2.", "\\(3.2 / 1.6 = 2\\)."),
        q("ex13-q5", 13, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( (2.5)^2 + (1.5)^2 \\)", 8.5, "8.5", 0.01, None, "6.25 + 2.25 = 8.50.", "\\(6.25 + 2.25 = 8.5\\)."),
        q("ex13-q6", 13, "fractions", "Fractions & Decimals", "numeric", "Simplify \\( \\frac{x^2 - 5x + 6}{x - 2} \\) at \\( x = 10 \\).", 7, "7", 0, None, "Reduces to x - 3. 10 - 3 = 7.", "\\(10 - 3 = 7\\)."),

        q("ex13-q7", 13, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 27^{2/3} \\)", 9, "9", 0, None, "(3)^2 = 9.", "\\(3^2 = 9\\)."),
        q("ex13-q8", 13, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 32^{3/5} \\)", 8, "8", 0, None, "(2)^3 = 8.", "\\(2^3 = 8\\)."),
        q("ex13-q9", 13, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{12^2 + 5^2} \\)", 13, "13", 0, None, "sqrt(144 + 25) = sqrt(169) = 13.", "\\(13\\)."),

        q("ex13-q10", 13, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 2^{2x - 1} = 32 \\)", 3, "3", 0, None, "2x - 1 = 5 => 2x = 6 => x = 3.", "\\(2x = 6 \\implies x = 3\\)."),
        q("ex13-q11", 13, "algebra", "Algebra & Equations", "numeric", "If \\( \\log_{10}(x) = 3 \\), what is \\( \\frac{x}{200} \\)?", 5, "5", 0, None, "x = 1000. 1000 / 200 = 5.", "\\(\\frac{1000}{200} = 5\\)."),
        q("ex13-q12", 13, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( 3x^2 - 14x - 5 = 0 \\).", 5, "5 (roots are -1/3, 5)", 0, None, "(3x + 1)(x - 5) = 0.", "\\((3x+1)(x-5) = 0\\). Positive root is 5."),

        q("ex13-q13", 13, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1240}{620} \\)", 2, "2", 0.01, None, "1240 / 620 = 2.", "\\(2\\)."),
        q("ex13-q14", 13, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6.63 \\times 10^{-34}}{2.21 \\times 10^{-24}} \\times 10^{10} \\)", 3, "3", 0.05, None, "3 * 10^(-10) * 10^10 = 3.", "\\(3\\)."),
        q("ex13-q15", 13, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{9 \\times 10^9 \\times (2 \\times 10^{-6})^2}{(0.3)^2} \\)", 0.4, "0.4", 0.01, None, "36*10^-3 / 0.09 = 0.4.", "\\(0.4\\).")
    ]
})

# Day 14: Standard Angles & Ratio Arithmetic
days_11_20.append({
    "id": 14, "title": "Day 14: Special Ratio Trigonometry (30°, 45°, 60°)", "difficulty": 3, "tier": "Intermediate",
    "questions": [
        q("ex14-q1", 14, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 100 \\times 0.5 \\)", 50, "50", 0, None, "Half of 100 is 50.", "\\(50\\)."),
        q("ex14-q2", 14, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 20\\sqrt{2} \\times \\frac{1}{\\sqrt{2}} \\)", 20, "20", 0, None, "sqrt(2) cancels.", "\\(20\\)."),
        q("ex14-q3", 14, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 40 \\times \\frac{\\sqrt{3}}{2} \\). (Use \\( \\sqrt{3} \\approx 1.732 \\))", 34.64, "34.64 (or 20√3)", 0.1, None, "20 * 1.732 = 34.64.", "\\(20 \\times 1.732 = 34.64\\)."),

        q("ex14-q4", 14, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( (\\sqrt{3})^2 - 1^2 \\)", 2, "2", 0, None, "3 - 1 = 2.", "\\(3 - 1 = 2\\)."),
        q("ex14-q5", 14, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 2 \\times 0.5 \\times \\frac{\\sqrt{3}}{2} \\times 10 \\). (Use \\( \\sqrt{3} \\approx 1.732 \\))", 8.66, "8.66 (or 5√3)", 0.05, None, "5 * 1.732 = 8.66.", "\\(5 \\times 1.732 = 8.66\\)."),
        q("ex14-q6", 14, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 40 \\times 5 \\times 0.5 \\)", 100, "100", 0, None, "200 * 0.5 = 100.", "\\(100\\)."),

        q("ex14-q7", 14, "powers", "Powers, Roots & Surds", "numeric", "Solve for \\( x \\): \\( \\sqrt{3} x = 6 \\). Enter as decimal to 2 places.", 3.46, "3.46 (or 2√3)", 0.05, None, "6 / sqrt(3) = 2*sqrt(3) ≈ 3.464.", "\\(2\\sqrt{3} \\approx 3.46\\)."),
        q("ex14-q8", 14, "powers", "Powers, Roots & Surds", "numeric", "Evaluate \\( \\frac{1}{\\sqrt{2} + 1} \\) to 2 decimal places. (Rationalize)", 0.41, "0.41 (√2 - 1)", 0.02, None, "sqrt(2) - 1 = 1.414 - 1 = 0.414.", "\\(\\sqrt{2} - 1 \\approx 0.414\\)."),
        q("ex14-q9", 14, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( \\frac{15^2}{5} \\)", 45, "45", 0, None, "225 / 5 = 45.", "\\(225 / 5 = 45\\)."),

        q("ex14-q10", 14, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( \\frac{x^2 - 16}{x + 4} = 6 \\)", 10, "10", 0, None, "x - 4 = 6 => x = 10.", "\\(x - 4 = 6 \\implies x = 10\\)."),
        q("ex14-q11", 14, "algebra", "Algebra & Equations", "numeric", "If \\( s = 0.5 \\), find \\( 1 - s^2 \\). Enter as decimal.", 0.75, "0.75 (or 3/4)", 0.01, None, "1 - 0.25 = 0.75.", "\\(1 - 0.25 = 0.75\\)."),
        q("ex14-q12", 14, "algebra", "Algebra & Equations", "numeric", "Find the larger root of \\( 2x^2 - 9x + 10 = 0 \\).", 2.5, "2.5 (roots are 2, 2.5)", 0.01, None, "(2x - 5)(x - 2) = 0.", "\\(2.5\\)."),

        q("ex14-q13", 14, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{20^2}{2 \\times 10} \\)", 20, "20", 0, None, "400 / 20 = 20.", "\\(20\\)."),
        q("ex14-q14", 14, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10^2}{2 \\times 10} \\)", 5, "5", 0, None, "100 / 20 = 5.", "\\(5\\)."),
        q("ex14-q15", 14, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 20 \\times 0.5 \\times 0.5 \\)", 5, "5", 0, None, "10 * 0.5 = 5.", "\\(5\\).")
    ]
})

# Day 15: The 3-4-5 Ratio Multipliers
days_11_20.append({
    "id": 15, "title": "Day 15: The 3-4-5 Decimal Ratios (0.6 & 0.8)", "difficulty": 3, "tier": "Intermediate",
    "questions": [
        q("ex15-q1", 15, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 50 \\times 0.6 \\)", 30, "30", 0, None, "50 * 0.6 = 30.", "\\(30\\)."),
        q("ex15-q2", 15, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 50 \\times 0.8 \\)", 40, "40", 0, None, "50 * 0.8 = 40.", "\\(40\\)."),
        q("ex15-q3", 15, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 25 \\times 0.8 \\)", 20, "20", 0, None, "25 * 0.8 = 20.", "\\(20\\)."),

        q("ex15-q4", 15, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 0.75 \\times 80 \\)", 60, "60", 0, None, "(3/4) * 80 = 60.", "\\(60\\)."),
        q("ex15-q5", 15, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 10 \\times 10 \\times 0.6 \\)", 60, "60", 0, None, "100 * 0.6 = 60.", "\\(60\\)."),
        q("ex15-q6", 15, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 10 \\times 10 \\times 0.8 \\)", 80, "80", 0, None, "100 * 0.8 = 80.", "\\(80\\)."),

        q("ex15-q7", 15, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{30^2 + 40^2} \\)", 50, "50", 0, None, "10 * sqrt(9 + 16) = 10 * 5 = 50.", "\\(50\\)."),
        q("ex15-q8", 15, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{60^2 + 80^2} \\)", 100, "100", 0, None, "20 * 5 = 100.", "\\(100\\)."),
        q("ex15-q9", 15, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 0.5 \\times 80 \\)", 40, "40", 0, None, "Half of 80 is 40.", "\\(40\\)."),

        q("ex15-q10", 15, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 0.8x - 0.6(x + 5) = 3 \\)", 30, "30", 0, None, "0.2x - 3 = 3 => 0.2x = 6 => x = 30.", "\\(x = 30\\)."),
        q("ex15-q11", 15, "algebra", "Algebra & Equations", "numeric", "Find the smaller positive root of \\( 4x^2 - 12x + 5 = 0 \\).", 0.5, "0.5 (roots are 0.5, 2.5)", 0.01, None, "(2x - 1)(2x - 5) = 0.", "\\(0.5\\)."),
        q("ex15-q12", 15, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( \\frac{x^2 - 25}{x - 5} = 12 \\)", 7, "7", 0, None, "x + 5 = 12 => x = 7.", "\\(x = 7\\)."),

        q("ex15-q13", 15, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 3(4) + 4(-3) \\)", 0, "0", 0, None, "12 - 12 = 0.", "\\(0\\)."),
        q("ex15-q14", 15, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 50 \\times 0.6 \\)", 30, "30", 0, None, "30.", "\\(30\\)."),
        q("ex15-q15", 15, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 50 \\times 0.8 \\)", 40, "40", 0, None, "40.", "\\(40\\).")
    ]
})

# Day 16: Multi-Dimensional Orthogonal Ratios
days_11_20.append({
    "id": 16, "title": "Day 16: Orthogonal Pythagorean Triples & Sum of Squares", "difficulty": 4, "tier": "Intermediate → Advanced",
    "questions": [
        q("ex16-q1", 16, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 10 \\times \\sqrt{3} \\) to 2 decimal places.", 17.32, "17.32 (or 10√3)", 0.05, None, "10 * 1.732 = 17.32.", "\\(17.32\\)."),
        q("ex16-q2", 16, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 2 \\times 20 \\times 0.5 \\)", 20, "20", 0, None, "20.", "\\(20\\)."),
        q("ex16-q3", 16, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 15^2 + 20^2 \\)", 625, "625", 0, None, "225 + 400 = 625.", "\\(625\\)."),

        q("ex16-q4", 16, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 6(3) + 8(2) \\)", 34, "34", 0, None, "18 + 16 = 34.", "\\(34\\)."),
        q("ex16-q5", 16, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( 18 \\times 2.5 \\times 4 \\)", 180, "180", 0, None, "2.5 * 4 = 10. 18 * 10 = 180.", "\\(180\\)."),
        q("ex16-q6", 16, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 20(3) + 15(2) \\)", 90, "90", 0, None, "60 + 30 = 90.", "\\(90\\)."),

        q("ex16-q7", 16, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{2^2 + 3^2 + 6^2} \\)", 7, "7", 0, None, "sqrt(4 + 9 + 36) = sqrt(49) = 7.", "\\(7\\)."),
        q("ex16-q8", 16, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{8^2 + 6^2} \\)", 10, "10", 0, None, "sqrt(64 + 36) = 10.", "\\(10\\)."),
        q("ex16-q9", 16, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{125.44} \\)", 11.2, "11.2", 0.05, None, "11.2^2 = 125.44.", "\\(11.2\\)."),

        q("ex16-q10", 16, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{5}{x-2} = \\frac{7}{x+4} \\)", 17, "17", 0, None, "5x + 20 = 7x - 14 => 2x = 34 => x = 17.", "\\(x = 17\\)."),
        q("ex16-q11", 16, "algebra", "Algebra & Equations", "numeric", "Find the larger root of \\( 6x^2 - 7x + 2 = 0 \\). Enter as decimal.", 0.67, "0.67 (or 2/3)", 0.02, None, "(2x - 1)(3x - 2) = 0 => 2/3 ≈ 0.667.", "\\(2/3 \\approx 0.67\\)."),
        q("ex16-q12", 16, "algebra", "Algebra & Equations", "numeric", "Solve for \\( c \\): \\( 2(6) + c(-4) = 0 \\)", 3, "3", 0, None, "12 - 4c = 0 => c = 3.", "\\(c = 3\\)."),

        q("ex16-q13", 16, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1.5 \\times 10^8}{3 \\times 10^5} \\)", 500, "500", 0.1, None, "0.5 * 10^3 = 500.", "\\(500\\)."),
        q("ex16-q14", 16, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 4 \\times 2^2 \\)", 16, "16", 0, None, "4 * 4 = 16.", "\\(16\\)."),
        q("ex16-q15", 16, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 0.5 \\times 0.5 \\times 16 \\)", 4, "4", 0, None, "0.25 * 16 = 4.", "\\(4\\).")
    ]
})

# Day 17: Inverse Square Ratios
days_11_20.append({
    "id": 17, "title": "Day 17: Inverse-Square Scaling & Power Multiplication", "difficulty": 4, "tier": "Intermediate → Advanced",
    "questions": [
        q("ex17-q1", 17, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{3^2} \\). Enter as decimal to 3 places.", 0.111, "0.111 (or 1/9)", 0.01, None, "1/9 ≈ 0.111.", "\\(0.111\\)."),
        q("ex17-q2", 17, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{(1/2)^2} \\)", 4, "4", 0, None, "1 / 0.25 = 4.", "\\(4\\)."),
        q("ex17-q3", 17, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 225 \\times 0.04 \\)", 9, "9", 0.01, None, "225 / 25 = 9.", "\\(9\\)."),

        q("ex17-q4", 17, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 1 - 2(0.01) \\)", 0.98, "0.98", 0.005, None, "1 - 0.02 = 0.98.", "\\(0.98\\)."),
        q("ex17-q5", 17, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 180 \\div 4 \\)", 45, "45", 0, None, "180 / 4 = 45.", "\\(45\\)."),
        q("ex17-q6", 17, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 4 \\times 12 \\)", 48, "48", 0, None, "48.", "\\(48\\)."),

        q("ex17-q7", 17, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 4^{3/2} \\)", 8, "8", 0, None, "(sqrt(4))^3 = 2^3 = 8.", "\\(8\\)."),
        q("ex17-q8", 17, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{1.96 \\times 10^6} \\)", 1400, "1400", 1, None, "1.4 * 1000 = 1400.", "\\(1400\\)."),
        q("ex17-q9", 17, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{64 \\times 10^6} \\)", 8000, "8000", 1, None, "8 * 1000 = 8000.", "\\(8000\\)."),

        q("ex17-q10", 17, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( r \\): \\( \\frac{3600}{r^2} = 400 \\)", 3, "3", 0, None, "r^2 = 9 => r = 3.", "\\(r = 3\\)."),
        q("ex17-q11", 17, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( 2x^2 - 18 = 0 \\)", 3, "3", 0, None, "x^2 = 9 => x = 3.", "\\(x = 3\\)."),
        q("ex17-q12", 17, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{x^2 - 49}{x - 7} = 20 \\)", 13, "13", 0, None, "x + 7 = 20 => x = 13.", "\\(x = 13\\)."),

        q("ex17-q13", 17, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{36}{0.04} \\)", 900, "900", 1, None, "3600 / 4 = 900.", "\\(900\\)."),
        q("ex17-q14", 17, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 0.5 \\times 400 \\times 10^{-6} \\times 2500 \\)", 0.5, "0.5", 0.01, None, "0.5 * 1 = 0.5.", "\\(0.5\\)."),
        q("ex17-q15", 17, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6.67 \\times 10^{-11} \\times 6 \\times 10^{24}}{(6.4 \\times 10^6)^2} \\) to 1 decimal place.", 9.8, "9.8", 0.2, None, "Approx 9.77 ≈ 9.8.", "\\(9.8\\).")
    ]
})

# Day 18: Surd Rationalization & Reciprocals
days_11_20.append({
    "id": 18, "title": "Day 18: Surd Rationalization & Reciprocal Sums", "difficulty": 4, "tier": "Intermediate → Advanced",
    "questions": [
        q("ex18-q1", 18, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{\\sqrt{3} + 1}{2} \\) to 2 decimal places.", 1.37, "1.37", 0.03, None, "(1.732 + 1)/2 = 1.366 ≈ 1.37.", "\\(1.37\\)."),
        q("ex18-q2", 18, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1.732}{2} + 0.134 \\)", 1, "1", 0.01, None, "0.866 + 0.134 = 1.", "\\(1\\)."),
        q("ex18-q3", 18, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 1.25 \\times 10^3 \\times 0.008 \\)", 10, "10", 0.01, None, "1250 * 0.008 = 10.", "\\(10\\)."),

        q("ex18-q4", 18, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{6 \\times 3}{6 + 3} \\)", 2, "2", 0.01, None, "18 / 9 = 2.", "\\(2\\)."),
        q("ex18-q5", 18, "fractions", "Fractions & Decimals", "numeric", "Evaluate \\( \\frac{1}{x-1} - \\frac{1}{x+1} \\) at \\( x = 3 \\). Enter decimal.", 0.25, "0.25 (or 1/4)", 0.01, None, "2 / (9 - 1) = 2/8 = 0.25.", "\\(0.25\\)."),
        q("ex18-q6", 18, "fractions", "Fractions & Decimals", "numeric", "If \\( \\alpha + \\beta = 7 \\) and \\( \\alpha\\beta = 12 \\), what is \\( \\frac{1}{\\alpha} + \\frac{1}{\\beta} \\)? Enter to 3 decimal places.", 0.583, "0.583 (or 7/12)", 0.01, None, "7 / 12 ≈ 0.583.", "\\(0.583\\)."),

        q("ex18-q7", 18, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{18} + \\sqrt{32} - \\sqrt{50} \\). Enter decimal to 2 places.", 2.83, "2.83 (or 2√2)", 0.05, None, "3*sqrt(2) + 4*sqrt(2) - 5*sqrt(2) = 2*sqrt(2) ≈ 2.828.", "\\(2.83\\)."),
        q("ex18-q8", 18, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 4 \\times 25 \\)", 100, "100", 0, None, "100.", "\\(100\\)."),
        q("ex18-q9", 18, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{40}{1 + 3} \\)", 10, "10", 0, None, "40 / 4 = 10.", "\\(10\\)."),

        q("ex18-q10", 18, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( \\frac{x}{x-2} + \\frac{x-2}{x} = \\frac{10}{3} \\)", 3, "3", 0.01, None, "Let y = x/(x-2). y + 1/y = 10/3 => y = 3 => x = 3.", "\\(x = 3\\)."),
        q("ex18-q11", 18, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 3^{x+1} + 3^x = 36 \\)", 2, "2", 0, None, "4 * 3^x = 36 => 3^x = 9 => x = 2.", "\\(x = 2\\)."),
        q("ex18-q12", 18, "algebra", "Algebra & Equations", "numeric", "Evaluate \\( \\frac{x^3 + 27}{x + 3} \\) at \\( x = 7 \\).", 37, "37", 0, None, "x^2 - 3x + 9 = 49 - 21 + 9 = 37.", "\\(37\\)."),

        q("ex18-q13", 18, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{144 \\times 10^{-3}}{0.36} \\)", 0.4, "0.4", 0.01, None, "144 / 360 = 0.4.", "\\(0.4\\)."),
        q("ex18-q14", 18, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{8.85 \\times 10^{-12} \\times 0.02}{1.77 \\times 10^{-3}} \\times 10^{12} \\)", 100, "100", 2, None, "10 * 10 = 100.", "\\(100\\)."),
        q("ex18-q15", 18, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 0.5 \\times 8.85 \\times 10^{-12} \\times 4 \\times 10^6 \\times 10^6 \\)", 17.7, "17.7", 0.2, None, "2 * 8.85 = 17.7.", "\\(17.7\\).")
    ]
})

# Day 19: Precision Decimal Operations
days_11_20.append({
    "id": 19, "title": "Day 19: Constant Evaluation & Subtraction Balancing", "difficulty": 4, "tier": "Intermediate → Advanced",
    "questions": [
        q("ex19-q1", 19, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 3.1416 \\times 25 \\) to 2 decimal places.", 78.54, "78.54", 0.2, None, "314.16 / 4 = 78.54.", "\\(78.54\\)."),
        q("ex19-q2", 19, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1240}{400} \\)", 3.1, "3.1", 0.02, None, "124 / 40 = 3.1.", "\\(3.1\\)."),
        q("ex19-q3", 19, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 3.1 - 2.1 \\)", 1, "1", 0, None, "1.0.", "\\(1\\)."),

        q("ex19-q4", 19, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{12.27}{\\sqrt{100}} \\)", 1.227, "1.227", 0.01, None, "12.27 / 10 = 1.227.", "\\(1.227\\)."),
        q("ex19-q5", 19, "fractions", "Fractions & Decimals", "numeric", "Simplify \\( \\frac{x^2 - y^2}{(x - y)^2} \\) when \\( x = 3.5 \\) and \\( y = 1.5 \\).", 2.5, "2.5 (or 5/2)", 0.01, None, "(x + y)/(x - y) = 5.0 / 2.0 = 2.5.", "\\(2.5\\)."),
        q("ex19-q6", 19, "fractions", "Fractions & Decimals", "numeric", "If \\( \\log_{10}(2) = 0.3010 \\), what is \\( \\log_{10}(8) \\)?", 0.903, "0.903", 0.005, None, "3 * 0.3010 = 0.903.", "\\(0.903\\)."),

        q("ex19-q7", 19, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( (1/2)^3 \\). Enter as decimal.", 0.125, "0.125 (or 1/8)", 0.005, None, "1/8 = 0.125.", "\\(0.125\\)."),
        q("ex19-q8", 19, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{1.6} \\) to 2 decimal places.", 1.26, "1.26 (or 1.265)", 0.05, None, "1.265^2 ≈ 1.60.", "\\(1.26\\)."),
        q("ex19-q9", 19, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 20 \\div 4 \\)", 5, "5", 0, None, "5.", "\\(5\\)."),

        q("ex19-q10", 19, "algebra", "Algebra & Equations", "numeric", "Solve for \\( \\lambda \\): \\( \\frac{1240}{\\lambda} = 5 \\)", 248, "248", 1, None, "lambda = 1240 / 5 = 248.", "\\(248\\)."),
        q("ex19-q11", 19, "algebra", "Algebra & Equations", "numeric", "Evaluate: \\( \\frac{0.693}{0.0693} \\)", 10, "10", 0.05, None, "10.", "\\(10\\)."),
        q("ex19-q12", 19, "algebra", "Algebra & Equations", "numeric", "Calculate: \\( 4.0 - 2.5 \\)", 1.5, "1.5", 0, None, "1.5.", "\\(1.5\\)."),

        q("ex19-q13", 19, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 0.02 \\times 931.5 \\) to 2 decimal places.", 18.63, "18.63", 0.2, None, "18.63.", "\\(18.63\\)."),
        q("ex19-q14", 19, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1240}{2} \\)", 620, "620", 0, None, "620.", "\\(620\\)."),
        q("ex19-q15", 19, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 16 \\times 0.0625 \\)", 1, "1", 0, None, "16 * 1/16 = 1.", "\\(1\\).")
    ]
})

# Day 20: Rapid Approximation Techniques
days_11_20.append({
    "id": 20, "title": "Day 20: Binomial Approximation & Error Propagation", "difficulty": 4, "tier": "Intermediate → Advanced",
    "questions": [
        q("ex20-q1", 20, "mental", "Mental Arithmetic", "numeric", "Evaluate \\( \\frac{1}{0.98} \\) using \\( (1 - x)^{-1} \\approx 1 + x \\).", 1.02, "1.02", 0.005, None, "1 + 0.02 = 1.02.", "\\(1.02\\)."),
        q("ex20-q2", 20, "mental", "Mental Arithmetic", "numeric", "Calculate \\( (1.02)^5 \\approx 1 + 5(0.02) \\). Enter decimal.", 1.1, "1.10", 0.01, None, "1 + 0.10 = 1.10.", "\\(1.1\\)."),
        q("ex20-q3", 20, "mental", "Mental Arithmetic", "numeric", "Estimate \\( \\sqrt{101} \\approx 10 + \\frac{1}{20} \\). Enter decimal.", 10.05, "10.05", 0.02, None, "10 + 0.05 = 10.05.", "\\(10.05\\)."),

        q("ex20-q4", 20, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 18.5 \\times 4.2 \\) to 1 decimal place.", 77.7, "77.7", 0.5, None, "74 + 3.7 = 77.7.", "\\(77.7\\)."),
        q("ex20-q5", 20, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 2.1^2 \\)", 4.41, "4.41", 0.01, None, "21^2 = 441 => 4.41.", "\\(4.41\\)."),
        q("ex20-q6", 20, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 100 \\div 3 \\) to 1 decimal place.", 33.3, "33.3", 0.5, None, "33.33.", "\\(33.3\\)."),

        q("ex20-q7", 20, "powers", "Powers, Roots & Surds", "numeric", "Using \\( \\pi^2 \\approx 10 \\), evaluate: \\( \\frac{40}{\\pi^2} \\)", 4, "4 (approx 4.05)", 0.2, None, "40 / 10 = 4.", "\\(4\\)."),
        q("ex20-q8", 20, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{1}{0.2} \\)", 5, "5", 0, None, "10 / 2 = 5.", "\\(5\\)."),
        q("ex20-q9", 20, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 5 - 2 \\)", 3, "3", 0, None, "3.", "\\(3\\)."),

        q("ex20-q10", 20, "algebra", "Algebra & Equations", "numeric", "If \\( A = 4\\pi r^2 \\) and \\( r \\) has \\( 2\\% \\) error, what is percentage error in \\( A \\)?", 4, "4%", 0, None, "2 * 2% = 4%.", "\\(4\\%\\)."),
        q("ex20-q11", 20, "algebra", "Algebra & Equations", "numeric", "If \\( V \\propto r^3 \\) and \\( r \\) has \\( 2\\% \\) error, what is percentage error in \\( V \\)?", 6, "6%", 0, None, "3 * 2% = 6%.", "\\(6\\%\\)."),
        q("ex20-q12", 20, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{2x}{x+3} = 1.6 \\)", 12, "12", 0.1, None, "2x = 1.6x + 4.8 => 0.4x = 4.8 => x = 12.", "\\(x = 12\\)."),

        q("ex20-q13", 20, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{340}{512} \\) to 2 decimal places.", 0.66, "0.66 (or 2/3)", 0.03, None, "340 / 512 ≈ 0.664.", "\\(0.66\\)."),
        q("ex20-q14", 20, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{4\\pi \\times 10^{-7} \\times 5}{2 \\times 0.1} \\times 10^5 \\) where \\( \\pi \\approx 3.14 \\).", 3.14, "3.14", 0.1, None, "pi * 10^-5 * 10^5 = pi ≈ 3.14.", "\\(3.14\\)."),
        q("ex20-q15", 20, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 0.5 \\times (2 + 1) \\)", 1.5, "1.5", 0.01, None, "0.5 * 3 = 1.5.", "\\(1.5\\).")
    ]
})

print(f"Days 11-20 created: {len(days_11_20)} exercises.")
