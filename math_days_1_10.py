# Days 1 - 10: Foundation to Basic Pure Mathematics Calculations
# 5 Sections in every exercise:
# 1. Mental Arithmetic (3 questions)
# 2. Fractions & Decimals (3 questions)
# 3. Powers, Roots & Surds (3 questions)
# 4. Algebra & Equations (3 questions)
# 5. Scientific Notation & Estimation (3 questions)
# Exactly 15 questions per exercise

def q(qid, ex_id, sec, sec_name, qtype, text, ans, disp_ans, tol=0.01, options=None, hint="", exp=""):
    item = {
        "id": qid,
        "exerciseId": ex_id,
        "section": sec,
        "sectionName": sec_name,
        "type": qtype,
        "question": text,
        "answer": ans,
        "displayAnswer": str(disp_ans),
        "tolerance": tol,
        "hint": hint,
        "explanation": exp
    }
    if qtype == "mcq":
        item["options"] = options or []
    return item

days_1_10 = []

# Day 1: Foundation 1
days_1_10.append({
    "id": 1, "title": "Day 01: Arithmetic Rebuild & Basic Roots", "difficulty": 1, "tier": "Foundation",
    "questions": [
        # 1. Mental Arithmetic
        q("ex1-q1", 1, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 17 \\times 6 \\)", 102, "102", 0, None, "Split as (10 + 7) * 6 = 60 + 42.", "\\(17 \\times 6 = (10 \\times 6) + (7 \\times 6) = 60 + 42 = 102\\)."),
        q("ex1-q2", 1, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 144 \\div 12 \\)", 12, "12", 0, None, "Recall 12 * 12 = 144.", "\\(144 \\div 12 = 12\\)."),
        q("ex1-q3", 1, "mental", "Mental Arithmetic", "numeric", "Calculate \\( 25\\% \\) of \\( 240 \\)", 60, "60", 0, None, "25% is 1/4. Divide 240 by 4.", "\\(240 \\div 4 = 60\\)."),
        # 2. Fractions & Decimals
        q("ex1-q4", 1, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 3.5 + 2.75 \\)", 6.25, "6.25", 0.01, None, "3.50 + 2.75 = 5.00 + 1.25.", "\\(3.50 + 2.75 = 6.25\\)."),
        q("ex1-q5", 1, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 0.8 \\times 0.25 \\)", 0.2, "0.2", 0.01, None, "0.25 is 1/4. Divide 0.8 by 4.", "\\(0.8 \\times \\frac{1}{4} = 0.2\\)."),
        q("ex1-q6", 1, "fractions", "Fractions & Decimals", "numeric", "Simplify \\( \\frac{18}{24} \\) to its decimal value.", 0.75, "0.75 (or 3/4)", 0.01, None, "Divide both by 6 to get 3/4.", "\\(\\frac{18}{24} = \\frac{3}{4} = 0.75\\)."),
        # 3. Powers, Roots & Surds
        q("ex1-q7", 1, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 14^2 \\)", 196, "196", 0, None, "14 * 14 = 196.", "\\(14^2 = 196\\)."),
        q("ex1-q8", 1, "powers", "Powers, Roots & Surds", "numeric", "Approximate \\( \\sqrt{2} \\) to 2 decimal places.", 1.41, "1.41 (or 1.414)", 0.02, None, "Memorize sqrt(2) ≈ 1.414.", "\\(\\sqrt{2} \\approx 1.414\\)."),
        q("ex1-q9", 1, "powers", "Powers, Roots & Surds", "numeric", "Approximate \\( \\sqrt{3} \\) to 2 decimal places.", 1.73, "1.73 (or 1.732)", 0.02, None, "Memorize sqrt(3) ≈ 1.732.", "\\(\\sqrt{3} \\approx 1.732\\)."),
        # 4. Algebra & Equations
        q("ex1-q10", 1, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 3x - 6 = 12 \\)", 6, "6", 0, None, "3x = 18 => x = 6.", "\\(3x = 18 \\implies x = 6\\)."),
        q("ex1-q11", 1, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( x^2 - 5x + 6 = 0 \\). Enter the larger root.", 3, "3 (roots are 2, 3)", 0, None, "(x - 2)(x - 3) = 0.", "\\((x-2)(x-3) = 0\\). Larger root is 3."),
        q("ex1-q12", 1, "algebra", "Algebra & Equations", "numeric", "Evaluate \\( 3(2x + 4) - 2(x - 1) \\) at \\( x = 2 \\).", 22, "22", 0, None, "Simplify to 4x + 14, then plug in 2.", "\\(4(2) + 14 = 22\\)."),
        # 5. Scientific Notation & Estimation
        q("ex1-q13", 1, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10^5 \\times 10^{-2}}{10^1} \\)", 100, "100 (or 10²)", 0.01, None, "Add exponents: 5 - 2 - 1 = 2.", "\\(10^{5 - 2 - 1} = 10^2 = 100\\)."),
        q("ex1-q14", 1, "scientific", "Scientific Notation & Estimation", "numeric", "Convert \\( \\frac{3}{8} \\) to its decimal equivalent.", 0.375, "0.375", 0.005, None, "3 * 0.125 = 0.375.", "\\(\\frac{3}{8} = 0.375\\)."),
        q("ex1-q15", 1, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( (2 \\times 10^3) \\times (4 \\times 10^2) \\). Enter numerical value.", 800000, "800,000 (or 8×10⁵)", 1, None, "(2 * 4) * 10^(3 + 2) = 8 * 10^5.", "\\(8 \\times 10^5 = 800,000\\).")
    ]
})

# Day 2: Foundation 2
days_1_10.append({
    "id": 2, "title": "Day 02: Decimal Operations & Linear Balance", "difficulty": 1, "tier": "Foundation",
    "questions": [
        # 1. Mental Arithmetic
        q("ex2-q1", 2, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 19 \\times 7 \\)", 133, "133", 0, None, "(20 - 1) * 7 = 140 - 7.", "\\(140 - 7 = 133\\)."),
        q("ex2-q2", 2, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 225 \\div 15 \\)", 15, "15", 0, None, "15^2 = 225.", "\\(225 \\div 15 = 15\\)."),
        q("ex2-q3", 2, "mental", "Mental Arithmetic", "numeric", "Calculate \\( 15\\% \\) of \\( 320 \\)", 48, "48", 0, None, "10% is 32, 5% is 16. 32 + 16 = 48.", "\\(32 + 16 = 48\\)."),
        # 2. Fractions & Decimals
        q("ex2-q4", 2, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 7.6 - 3.85 \\)", 3.75, "3.75", 0.01, None, "7.60 - 3.85.", "\\(7.60 - 3.85 = 3.75\\)."),
        q("ex2-q5", 2, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 1.2 \\times 0.5 \\)", 0.6, "0.6", 0.01, None, "Half of 1.2 is 0.6.", "\\(1.2 \\div 2 = 0.6\\)."),
        q("ex2-q6", 2, "fractions", "Fractions & Decimals", "numeric", "Convert \\( 0.625 \\) to fraction \\( \\frac{a}{b} \\). What is denominator \\( b \\)?", 8, "8 (Fraction is 5/8)", 0, None, "5 * 0.125 = 5/8.", "\\(0.625 = \\frac{5}{8}\\). Denominator is 8."),
        # 3. Powers, Roots & Surds
        q("ex2-q7", 2, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 16^2 \\)", 256, "256", 0, None, "16 * 16 = 256.", "\\(16^2 = 256\\)."),
        q("ex2-q8", 2, "powers", "Powers, Roots & Surds", "numeric", "Approximate \\( \\sqrt{5} \\) to 2 decimal places.", 2.24, "2.24 (or 2.236)", 0.02, None, "Memorize sqrt(5) ≈ 2.236.", "\\(\\sqrt{5} \\approx 2.236 \\approx 2.24\\)."),
        q("ex2-q9", 2, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\frac{10^7 \\times 10^{-3}}{10^2} \\)", 100, "100 (or 10²)", 0.01, None, "7 - 3 - 2 = 2.", "\\(10^2 = 100\\)."),
        # 4. Algebra & Equations
        q("ex2-q10", 2, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 4x - 7 = 21 \\)", 7, "7", 0, None, "4x = 28 => x = 7.", "\\(4x = 28 \\implies x = 7\\)."),
        q("ex2-q11", 2, "algebra", "Algebra & Equations", "numeric", "Evaluate \\( (x - 3)^2 \\) when \\( x = 8 \\).", 25, "25", 0, None, "(8 - 3)^2 = 5^2.", "\\(5^2 = 25\\)."),
        q("ex2-q12", 2, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{x}{5} + 3 = 11 \\)", 40, "40", 0, None, "x/5 = 8 => x = 40.", "\\(x = 8 \\times 5 = 40\\)."),
        # 5. Scientific Notation & Estimation
        q("ex2-q13", 2, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{4.8 \\times 10^6}{1.2 \\times 10^3} \\). Enter numerical value.", 4000, "4000 (or 4×10³)", 0.1, None, "(4.8 / 1.2) * 10^(6 - 3) = 4 * 10^3.", "\\(4 \\times 10^3 = 4000\\)."),
        q("ex2-q14", 2, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 120 \\times 0.05 \\)", 6, "6", 0.01, None, "10% is 12, 5% is 6.", "\\(120 \\times 0.05 = 6\\)."),
        q("ex2-q15", 2, "scientific", "Scientific Notation & Estimation", "numeric", "Approximate \\( \\sqrt{10} \\) to 2 decimal places. (Recall \\( \\pi^2 \\approx 10 \\))", 3.16, "3.16 (or 3.162)", 0.02, None, "sqrt(10) ≈ 3.162.", "\\(\\sqrt{10} \\approx 3.162 \\approx 3.16\\).")
    ]
})

# Day 3: Foundation 3
days_1_10.append({
    "id": 3, "title": "Day 03: Percentages & Squares (17² to 19²)", "difficulty": 1, "tier": "Foundation",
    "questions": [
        # 1. Mental Arithmetic
        q("ex3-q1", 3, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 23 \\times 4 \\)", 92, "92", 0, None, "20 * 4 + 3 * 4 = 80 + 12.", "\\(80 + 12 = 92\\)."),
        q("ex3-q2", 3, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 196 \\div 14 \\)", 14, "14", 0, None, "14^2 = 196.", "\\(196 \\div 14 = 14\\)."),
        q("ex3-q3", 3, "mental", "Mental Arithmetic", "numeric", "Calculate \\( 30\\% \\) of \\( 450 \\)", 135, "135", 0, None, "10% is 45. 45 * 3 = 135.", "\\(45 \\times 3 = 135\\)."),
        # 2. Fractions & Decimals
        q("ex3-q4", 3, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 4.25 + 6.85 \\)", 11.1, "11.1", 0.01, None, "4 + 6 = 10; 0.25 + 0.85 = 1.10.", "\\(10 + 1.10 = 11.10\\)."),
        q("ex3-q5", 3, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 0.6 \\times 0.15 \\)", 0.09, "0.09", 0.005, None, "6 * 15 = 90. Shift 3 places.", "\\(0.6 \\times 0.15 = 0.09\\)."),
        q("ex3-q6", 3, "fractions", "Fractions & Decimals", "numeric", "Convert \\( \\frac{7}{20} \\) to its decimal equivalent.", 0.35, "0.35", 0.005, None, "Multiply by 5/5: 35/100.", "\\(\\frac{35}{100} = 0.35\\)."),
        # 3. Powers, Roots & Surds
        q("ex3-q7", 3, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 17^2 \\)", 289, "289", 0, None, "17 * 17 = 289.", "\\(17^2 = 289\\)."),
        q("ex3-q8", 3, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 18^2 \\)", 324, "324", 0, None, "18 * 18 = 324.", "\\(18^2 = 324\\)."),
        q("ex3-q9", 3, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 19^2 \\)", 361, "361", 0, None, "(20 - 1)^2 = 400 - 40 + 1.", "\\(19^2 = 361\\)."),
        # 4. Algebra & Equations
        q("ex3-q10", 3, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 5x + 9 = 44 \\)", 7, "7", 0, None, "5x = 35 => x = 7.", "\\(5x = 35 \\implies x = 7\\)."),
        q("ex3-q11", 3, "algebra", "Algebra & Equations", "numeric", "Find the smaller root of \\( x^2 - 7x + 12 = 0 \\).", 3, "3 (roots are 3, 4)", 0, None, "(x - 3)(x - 4) = 0.", "\\((x-3)(x-4) = 0\\). Smaller root is 3."),
        q("ex3-q12", 3, "algebra", "Algebra & Equations", "numeric", "Simplify \\( \\frac{x^2 - 4}{x - 2} \\) at \\( x = 5 \\).", 7, "7", 0, None, "Reduces to x + 2. 5 + 2 = 7.", "\\(5 + 2 = 7\\)."),
        # 5. Scientific Notation & Estimation
        q("ex3-q13", 3, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 10^6 \\times 10^{-4} \\)", 100, "100 (or 10²)", 0.01, None, "6 - 4 = 2.", "\\(10^2 = 100\\)."),
        q("ex3-q14", 3, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10^8}{10^5} \\)", 1000, "1000 (or 10³)", 0.01, None, "8 - 5 = 3.", "\\(10^3 = 1000\\)."),
        q("ex3-q15", 3, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 0.04 \\times 2500 \\)", 100, "100", 0.01, None, "4 * 25 = 100.", "\\(0.04 \\times 2500 = 100\\).")
    ]
})

# Day 4: Foundation 4
days_1_10.append({
    "id": 4, "title": "Day 04: Fractions to Decimals & Linear Expansion", "difficulty": 1, "tier": "Foundation",
    "questions": [
        # 1. Mental Arithmetic
        q("ex4-q1", 4, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 16 \\times 8 \\)", 128, "128", 0, None, "2^4 * 2^3 = 2^7 = 128.", "\\(16 \\times 8 = 128\\)."),
        q("ex4-q2", 4, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 169 \\div 13 \\)", 13, "13", 0, None, "13^2 = 169.", "\\(169 \\div 13 = 13\\)."),
        q("ex4-q3", 4, "mental", "Mental Arithmetic", "numeric", "Calculate \\( 12.5\\% \\) of \\( 160 \\)", 20, "20", 0, None, "12.5% is 1/8. 160 / 8 = 20.", "\\(160 \\div 8 = 20\\)."),
        # 2. Fractions & Decimals
        q("ex4-q4", 4, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 9.1 - 4.45 \\)", 4.65, "4.65", 0.01, None, "9.10 - 4.45 = 4.65.", "\\(9.10 - 4.45 = 4.65\\)."),
        q("ex4-q5", 4, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 1.5 \\times 0.04 \\)", 0.06, "0.06", 0.005, None, "15 * 4 = 60. Shift 3 places.", "\\(0.060 = 0.06\\)."),
        q("ex4-q6", 4, "fractions", "Fractions & Decimals", "numeric", "Convert \\( \\frac{5}{16} \\) to its decimal value.", 0.3125, "0.3125", 0.005, None, "5 * 0.0625 = 0.3125.", "\\(\\frac{5}{16} = 0.3125\\)."),
        # 3. Powers, Roots & Surds
        q("ex4-q7", 4, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 20^2 - 15^2 \\)", 175, "175", 0, None, "(20 - 15)(20 + 15) = 5 * 35.", "\\(5 \\times 35 = 175\\)."),
        q("ex4-q8", 4, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{1.44} \\)", 1.2, "1.2", 0.01, None, "12^2 = 144.", "\\(\\sqrt{1.44} = 1.2\\)."),
        q("ex4-q9", 4, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 10^{-3} \\times 10^7 \\)", 10000, "10,000 (or 10⁴)", 1, None, "-3 + 7 = 4.", "\\(10^4 = 10,000\\)."),
        # 4. Algebra & Equations
        q("ex4-q10", 4, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 7x - 15 = 34 \\)", 7, "7", 0, None, "7x = 49 => x = 7.", "\\(7x = 49 \\implies x = 7\\)."),
        q("ex4-q11", 4, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{2x + 6}{4} = 5 \\)", 7, "7", 0, None, "2x + 6 = 20 => 2x = 14.", "\\(2x = 14 \\implies x = 7\\)."),
        q("ex4-q12", 4, "algebra", "Algebra & Equations", "numeric", "Expand \\( (x + 5)(x - 5) \\). What is value at \\( x = 7 \\)?", 24, "24", 0, None, "x^2 - 25 = 49 - 25 = 24.", "\\(49 - 25 = 24\\)."),
        # 5. Scientific Notation & Estimation
        q("ex4-q13", 4, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{3.6 \\times 10^4}{9 \\times 10^1} \\)", 400, "400", 0.1, None, "(3.6 / 9) * 10^(4 - 1) = 0.4 * 1000.", "\\(0.4 \\times 1000 = 400\\)."),
        q("ex4-q14", 4, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( 2.5 \\times 10^{-2} \\times 400 \\)", 10, "10", 0.01, None, "2.5 * 4 = 10.", "\\(0.025 \\times 400 = 10\\)."),
        q("ex4-q15", 4, "scientific", "Scientific Notation & Estimation", "numeric", "Convert \\( \\frac{9}{25} \\) to its decimal equivalent.", 0.36, "0.36", 0.005, None, "9 * 4 / 100 = 0.36.", "\\(\\frac{36}{100} = 0.36\\).")
    ]
})

# Day 5: Foundation 5
days_1_10.append({
    "id": 5, "title": "Day 05: Benchmark Fluency Consolidation", "difficulty": 1, "tier": "Foundation",
    "questions": [
        # 1. Mental Arithmetic
        q("ex5-q1", 5, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 24 \\times 5 \\)", 120, "120", 0, None, "Half of 24 is 12, times 10 = 120.", "\\(24 \\times 5 = 120\\)."),
        q("ex5-q2", 5, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 256 \\div 16 \\)", 16, "16", 0, None, "16^2 = 256.", "\\(256 \\div 16 = 16\\)."),
        q("ex5-q3", 5, "mental", "Mental Arithmetic", "numeric", "Calculate \\( 40\\% \\) of \\( 350 \\)", 140, "140", 0, None, "35 * 4 = 140.", "\\(35 \\times 4 = 140\\)."),
        # 2. Fractions & Decimals
        q("ex5-q4", 5, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 5.35 + 8.75 \\)", 14.1, "14.1", 0.01, None, "5 + 8 = 13; 0.35 + 0.75 = 1.10.", "\\(13 + 1.10 = 14.1\\)."),
        q("ex5-q5", 5, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 0.75 \\times 0.8 \\)", 0.6, "0.6", 0.01, None, "3/4 of 0.8 = 0.6.", "\\(0.75 \\times 0.8 = 0.6\\)."),
        q("ex5-q6", 5, "fractions", "Fractions & Decimals", "numeric", "Simplify \\( \\frac{48}{72} \\) to lowest terms. Express as decimal.", 0.667, "0.667 (or 2/3)", 0.01, None, "Divide both by 24: 2/3 ≈ 0.667.", "\\(\\frac{2}{3} \\approx 0.667\\)."),
        # 3. Powers, Roots & Surds
        q("ex5-q7", 5, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 21^2 \\)", 441, "441", 0, None, "21 * 21 = 441.", "\\(21^2 = 441\\)."),
        q("ex5-q8", 5, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{0.04} \\)", 0.2, "0.2", 0.01, None, "0.2 * 0.2 = 0.04.", "\\(\\sqrt{0.04} = 0.2\\)."),
        q("ex5-q9", 5, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 5^3 \\)", 125, "125", 0, None, "5 * 5 * 5 = 125.", "\\(5^3 = 125\\)."),
        # 4. Algebra & Equations
        q("ex5-q10", 5, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 3(x + 4) = 27 \\)", 5, "5", 0, None, "x + 4 = 9 => x = 5.", "\\(x + 4 = 9 \\implies x = 5\\)."),
        q("ex5-q11", 5, "algebra", "Algebra & Equations", "numeric", "Find the larger root of \\( x^2 - 8x + 15 = 0 \\).", 5, "5 (roots are 3, 5)", 0, None, "(x - 3)(x - 5) = 0.", "\\((x-3)(x-5) = 0\\). Larger root is 5."),
        q("ex5-q12", 5, "algebra", "Algebra & Equations", "numeric", "If \\( \\frac{a}{b} = \\frac{3}{4} \\) and \\( b = 28 \\), find \\( a \\).", 21, "21", 0, None, "(3/4) * 28 = 21.", "\\(a = \\frac{3}{4} \\times 28 = 21\\)."),
        # 5. Scientific Notation & Estimation
        q("ex5-q13", 5, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6.4 \\times 10^5}{1.6 \\times 10^2} \\). Enter numerical value.", 4000, "4000 (or 4×10³)", 0.1, None, "4 * 10^3 = 4000.", "\\(4 \\times 10^3 = 4000\\)."),
        q("ex5-q14", 5, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 125 \\times 0.08 \\)", 10, "10", 0.01, None, "125 * 8 = 1000. Shift 2 places.", "\\(125 \\times 0.08 = 10\\)."),
        q("ex5-q15", 5, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{10^9 \\times 10^{-6}}{10^1} \\)", 100, "100 (or 10²)", 0.01, None, "9 - 6 - 1 = 2.", "\\(10^2 = 100\\).")
    ]
})

# Day 6: Basic -> Intermediate 1
days_1_10.append({
    "id": 6, "title": "Day 06: Mixed Numbers, Ratios & Squares (21² to 23²)", "difficulty": 2, "tier": "Basic → Intermediate",
    "questions": [
        # 1. Mental Arithmetic
        q("ex6-q1", 6, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 18 \\times 15 \\)", 270, "270", 0, None, "18 * 10 + 90 = 270.", "\\(180 + 90 = 270\\)."),
        q("ex6-q2", 6, "mental", "Mental Arithmetic", "numeric", "Divide 240 in ratio \\( 3 : 5 \\). What is the smaller part?", 90, "90", 0, None, "8 parts = 240 => 1 part = 30. 3 * 30 = 90.", "\\(3 \\times 30 = 90\\)."),
        q("ex6-q3", 6, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( (-15) + (-27) - (-12) \\)", -30, "-30", 0, None, "-42 + 12 = -30.", "\\(-42 + 12 = -30\\)."),
        # 2. Fractions & Decimals
        q("ex6-q4", 6, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( 3\\frac{1}{2} + 2\\frac{3}{4} \\). Enter as decimal.", 6.25, "6.25 (or 25/4)", 0.01, None, "3.50 + 2.75 = 6.25.", "\\(3.5 + 2.75 = 6.25\\)."),
        q("ex6-q5", 6, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 35\\% \\) of \\( 600 \\)", 210, "210", 0, None, "35 * 6 = 210.", "\\(35 \\times 6 = 210\\)."),
        q("ex6-q6", 6, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{0.72}{0.09} \\)", 8, "8", 0, None, "72 / 9 = 8.", "\\(72 \\div 9 = 8\\)."),
        # 3. Powers, Roots & Surds
        q("ex6-q7", 6, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 22^2 \\)", 484, "484", 0, None, "22 * 22 = 484.", "\\(22^2 = 484\\)."),
        q("ex6-q8", 6, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 6^3 \\)", 216, "216", 0, None, "36 * 6 = 216.", "\\(6^3 = 216\\)."),
        q("ex6-q9", 6, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{0.0081} \\)", 0.09, "0.09", 0.001, None, "9^2 = 81. 4 decimal places -> 2 places.", "\\(\\sqrt{0.0081} = 0.09\\)."),
        # 4. Algebra & Equations
        q("ex6-q10", 6, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{x - 3}{4} = \\frac{x + 1}{6} \\)", 11, "11", 0, None, "6(x - 3) = 4(x + 1) => 2x = 22.", "\\(2x = 22 \\implies x = 11\\)."),
        q("ex6-q11", 6, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 2x - 3(x - 4) = 7 \\)", 5, "5", 0, None, "-x + 12 = 7 => x = 5.", "\\(-x + 12 = 7 \\implies x = 5\\)."),
        q("ex6-q12", 6, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( 2x^2 - 8 = 0 \\).", 2, "2", 0, None, "x^2 = 4 => x = 2.", "\\(x^2 = 4 \\implies x = 2\\)."),
        # 5. Scientific Notation & Estimation
        q("ex6-q13", 6, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1.6 \\times 10^{-19} \\times 10^3}{2 \\times 10^{-17}} \\)", 8, "8", 0.01, None, "0.8 * 10^(-16 - (-17)) = 0.8 * 10 = 8.", "\\(0.8 \\times 10 = 8\\)."),
        q("ex6-q14", 6, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 45 \\times 12 \\)", 540, "540", 0, None, "45 * 10 + 90 = 540.", "\\(450 + 90 = 540\\)."),
        q("ex6-q15", 6, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( (-4) \\times (-7) - 3 \\times 8 \\)", 4, "4", 0, None, "28 - 24 = 4.", "\\(28 - 24 = 4\\).")
    ]
})

# Day 7: Basic -> Intermediate 2
days_1_10.append({
    "id": 7, "title": "Day 07: Difference of Squares & Multi-Step Fractions", "difficulty": 2, "tier": "Basic → Intermediate",
    "questions": [
        # 1. Mental Arithmetic
        q("ex7-q1", 7, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 32 \\times 15 \\)", 480, "480", 0, None, "320 + 160 = 480.", "\\(320 + 160 = 480\\)."),
        q("ex7-q2", 7, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 17.5\\% \\) of \\( 400 \\)", 70, "70", 0, None, "17.5 * 4 = 70.", "\\(17.5 \\times 4 = 70\\)."),
        q("ex7-q3", 7, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 25^2 - 24^2 \\)", 49, "49", 0, None, "(25 - 24)(25 + 24) = 1 * 49.", "\\(1 \\times 49 = 49\\)."),
        # 2. Fractions & Decimals
        q("ex7-q4", 7, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 4\\frac{1}{3} - 1\\frac{5}{6} \\). Enter as decimal.", 2.5, "2.5 (or 5/2)", 0.02, None, "26/6 - 11/6 = 15/6 = 2.5.", "\\(\\frac{15}{6} = 2.5\\)."),
        q("ex7-q5", 7, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{5}{12} + \\frac{7}{18} \\). Enter as decimal to 3 places.", 0.806, "0.806 (or 29/36)", 0.01, None, "LCM is 36. (15 + 14)/36 = 29/36 ≈ 0.806.", "\\(\\frac{29}{36} \\approx 0.806\\)."),
        q("ex7-q6", 7, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 62.5\\% \\) of \\( 400 \\)", 250, "250", 0, None, "5/8 * 400 = 5 * 50 = 250.", "\\(\\frac{5}{8} \\times 400 = 250\\)."),
        # 3. Powers, Roots & Surds
        q("ex7-q7", 7, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 23^2 \\)", 529, "529", 0, None, "23 * 23 = 529.", "\\(23^2 = 529\\)."),
        q("ex7-q8", 7, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 7^3 \\)", 343, "343", 0, None, "49 * 7 = 343.", "\\(7^3 = 343\\)."),
        q("ex7-q9", 7, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( 52^2 - 48^2 \\)", 400, "400", 0, None, "(52 - 48)(52 + 48) = 4 * 100.", "\\(4 \\times 100 = 400\\)."),
        # 4. Algebra & Equations
        q("ex7-q10", 7, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( 4(3x - 2) = 2(5x + 4) \\)", 8, "8", 0, None, "12x - 8 = 10x + 8 => 2x = 16.", "\\(2x = 16 \\implies x = 8\\)."),
        q("ex7-q11", 7, "algebra", "Algebra & Equations", "numeric", "Find the larger root of \\( x^2 - 11x + 28 = 0 \\).", 7, "7 (roots are 4, 7)", 0, None, "(x - 4)(x - 7) = 0.", "\\((x-4)(x-7) = 0\\). Larger root is 7."),
        q("ex7-q12", 7, "algebra", "Algebra & Equations", "numeric", "Solve for \\( y \\) if \\( 3x + 2y = 26 \\) and \\( x = 4 \\).", 7, "7", 0, None, "12 + 2y = 26 => 2y = 14.", "\\(2y = 14 \\implies y = 7\\)."),
        # 5. Scientific Notation & Estimation
        q("ex7-q13", 7, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{3.6 \\times 10^{-5}}{9 \\times 10^{-8}} \\)", 400, "400", 0.1, None, "0.4 * 10^3 = 400.", "\\(0.4 \\times 10^3 = 400\\)."),
        q("ex7-q14", 7, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 12.4 - 3.75 - 2.65 \\)", 6, "6", 0.01, None, "3.75 + 2.65 = 6.40. 12.40 - 6.40 = 6.", "\\(12.4 - 6.4 = 6\\)."),
        q("ex7-q15", 7, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 56 \\times 25 \\)", 1400, "1400", 0, None, "56 / 4 * 100 = 14 * 100 = 1400.", "\\(14 \\times 100 = 1400\\).")
    ]
})

# Day 8: Basic -> Intermediate 3
days_1_10.append({
    "id": 8, "title": "Day 08: Squares (24² to 25²), Cubes & Ratios", "difficulty": 2, "tier": "Basic → Intermediate",
    "questions": [
        # 1. Mental Arithmetic
        q("ex8-q1", 8, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 37.5\\% \\) of \\( 480 \\)", 180, "180", 0, None, "3/8 * 480 = 3 * 60 = 180.", "\\(\\frac{3}{8} \\times 480 = 180\\)."),
        q("ex8-q2", 8, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 0.04 \\times 0.05 \\times 200 \\)", 0.4, "0.4", 0.01, None, "0.05 * 200 = 10. 0.04 * 10 = 0.4.", "\\(0.04 \\times 10 = 0.4\\)."),
        q("ex8-q3", 8, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 36 \\times 25 \\)", 900, "900", 0, None, "36 / 4 * 100 = 900.", "\\(9 \\times 100 = 900\\)."),
        # 2. Fractions & Decimals
        q("ex8-q4", 8, "fractions", "Fractions & Decimals", "numeric", "Solve for \\( x \\): \\( \\frac{3}{x} = \\frac{12}{28} \\)", 7, "7", 0, None, "12/28 simplifies to 3/7 => x = 7.", "\\(x = 7\\)."),
        q("ex8-q5", 8, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 87.5\\% \\) of \\( 320 \\)", 280, "280", 0, None, "7/8 * 320 = 7 * 40 = 280.", "\\(\\frac{7}{8} \\times 320 = 280\\)."),
        q("ex8-q6", 8, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 15.6 + 8.75 - 4.35 \\)", 20, "20", 0.01, None, "15.60 + 4.40 = 20.00.", "\\(15.6 + 4.4 = 20\\)."),
        # 3. Powers, Roots & Surds
        q("ex8-q7", 8, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 24^2 \\)", 576, "576", 0, None, "24 * 24 = 576.", "\\(24^2 = 576\\)."),
        q("ex8-q8", 8, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 8^3 \\)", 512, "512", 0, None, "64 * 8 = 512.", "\\(8^3 = 512\\)."),
        q("ex8-q9", 8, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 25^2 \\)", 625, "625", 0, None, "25 * 25 = 625.", "\\(25^2 = 625\\)."),
        # 4. Algebra & Equations
        q("ex8-q10", 8, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( x^2 - 4x - 21 = 0 \\).", 7, "7 (roots are -3, 7)", 0, None, "(x - 7)(x + 3) = 0.", "\\((x-7)(x+3) = 0\\). Positive root is 7."),
        q("ex8-q11", 8, "algebra", "Algebra & Equations", "numeric", "Solve for \\( x \\): \\( \\frac{2x - 5}{3} = \\frac{x + 7}{2} \\)", 31, "31", 0, None, "4x - 10 = 3x + 21 => x = 31.", "\\(4x - 10 = 3x + 21 \\implies x = 31\\)."),
        q("ex8-q12", 8, "algebra", "Algebra & Equations", "numeric", "Find the positive root of \\( 4x^2 - 36 = 0 \\).", 3, "3", 0, None, "x^2 = 9 => x = 3.", "\\(x = 3\\)."),
        # 5. Scientific Notation & Estimation
        q("ex8-q13", 8, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{6.4 \\times 10^8}{1.6 \\times 10^3} \\)", 400000, "400,000 (or 4×10⁵)", 1, None, "4 * 10^5 = 400000.", "\\(4 \\times 10^5 = 400,000\\)."),
        q("ex8-q14", 8, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1.44}{0.12} \\)", 12, "12", 0.01, None, "144 / 12 = 12.", "\\(1.44 / 0.12 = 12\\)."),
        q("ex8-q15", 8, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{(3 \\times 10^4) \\times (4 \\times 10^{-2})}{2 \\times 10^1} \\)", 60, "60", 0.01, None, "(12 / 2) * 10^(4 - 2 - 1) = 6 * 10^1 = 60.", "\\(6 \\times 10 = 60\\).")
    ]
})

# Day 9: Basic -> Intermediate 4
days_1_10.append({
    "id": 9, "title": "Day 09: Surd Multiplications & Quadratic Shortcuts", "difficulty": 2, "tier": "Basic → Intermediate",
    "questions": [
        # 1. Mental Arithmetic
        q("ex9-q1", 9, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( 75^2 - 25^2 \\)", 5000, "5000", 0, None, "(75 - 25)(75 + 25) = 50 * 100.", "\\(50 \\times 100 = 5000\\)."),
        q("ex9-q2", 9, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 48 \\times 12.5 \\)", 600, "600", 0, None, "48 / 8 * 100 = 600.", "\\(6 \\times 100 = 600\\)."),
        q("ex9-q3", 9, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 16.8 \\div 1.4 \\)", 12, "12", 0.01, None, "168 / 14 = 12.", "\\(168 \\div 14 = 12\\)."),
        # 2. Fractions & Decimals
        q("ex9-q4", 9, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{7}{15} - \\frac{2}{5} + \\frac{1}{3} \\). Enter as decimal.", 0.4, "0.4 (or 2/5)", 0.01, None, "(7 - 6 + 5)/15 = 6/15 = 2/5 = 0.4.", "\\(\\frac{6}{15} = 0.4\\)."),
        q("ex9-q5", 9, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 4.5^2 \\)", 20.25, "20.25", 0.01, None, "4 * 5 = 20 => 20.25.", "\\(4.5^2 = 20.25\\)."),
        q("ex9-q6", 9, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 64 \\times 3.5 \\)", 224, "224", 0, None, "64 * 3 + 32 = 192 + 32 = 224.", "\\(64 \\times 3.5 = 224\\)."),
        # 3. Powers, Roots & Surds
        q("ex9-q7", 9, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 9^3 \\)", 729, "729", 0, None, "81 * 9 = 729.", "\\(9^3 = 729\\)."),
        q("ex9-q8", 9, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 10^3 \\)", 1000, "1000", 0, None, "10 * 10 * 10 = 1000.", "\\(10^3 = 1000\\)."),
        q("ex9-q9", 9, "powers", "Powers, Roots & Surds", "numeric", "Simplify: \\( \\sqrt{75} - \\sqrt{12} \\). Express as \\( k\\sqrt{3} \\). Enter \\( k \\).", 3, "3 (3√3)", 0, None, "5*sqrt(3) - 2*sqrt(3) = 3*sqrt(3).", "\\(5\\sqrt{3} - 2\\sqrt{3} = 3\\sqrt{3}\\)."),
        # 4. Algebra & Equations
        q("ex9-q10", 9, "algebra", "Algebra & Equations", "numeric", "Solve the system for \\( x \\): \\( 2x + 3y = 13 \\) and \\( x - y = 4 \\).", 5, "5", 0, None, "y = x - 4. 2x + 3(x - 4) = 13 => 5x = 25.", "\\(5x = 25 \\implies x = 5\\)."),
        q("ex9-q11", 9, "algebra", "Algebra & Equations", "numeric", "Find \\( y \\) from the system: \\( 2x + 3y = 13 \\) and \\( x - y = 4 \\).", 1, "1", 0, None, "y = 5 - 4 = 1.", "\\(y = 1\\)."),
        q("ex9-q12", 9, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( \\frac{1}{x} + \\frac{1}{2x} = \\frac{3}{8} \\)", 4, "4", 0, None, "3/(2x) = 3/8 => 2x = 8 => x = 4.", "\\(2x = 8 \\implies x = 4\\)."),
        # 5. Scientific Notation & Estimation
        q("ex9-q13", 9, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{1.6 \\times 10^{-19} \\times 3 \\times 10^8}{6.4 \\times 10^{-7}} \\times 10^4 \\)", 7.5, "7.5", 0.05, None, "(4.8 / 6.4) * 10^(-11 - (-7) + 4) = 0.75 * 10 = 7.5.", "\\(0.75 \\times 10 = 7.5\\)."),
        q("ex9-q14", 9, "scientific", "Scientific Notation & Estimation", "numeric", "Convert speed ratio \\( \\frac{72}{18} \\times 5 \\)", 20, "20", 0, None, "4 * 5 = 20.", "\\(4 \\times 5 = 20\\)."),
        q("ex9-q15", 9, "scientific", "Scientific Notation & Estimation", "numeric", "Convert speed ratio \\( \\frac{25}{5} \\times 18 \\)", 90, "90", 0, None, "5 * 18 = 90.", "\\(5 \\times 18 = 90\\).")
    ]
})

# Day 10: Basic -> Intermediate 5
days_1_10.append({
    "id": 10, "title": "Day 10: Reciprocals, Squares (26² to 27²) & Factorization", "difficulty": 2, "tier": "Basic → Intermediate",
    "questions": [
        # 1. Mental Arithmetic
        q("ex10-q1", 10, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 72 \\times 1.25 \\)", 90, "90", 0, None, "72 + 18 = 90.", "\\(72 \\times 1.25 = 90\\)."),
        q("ex10-q2", 10, "mental", "Mental Arithmetic", "numeric", "Evaluate: \\( \\frac{1}{\\frac{1}{3} + \\frac{1}{6}} \\)", 2, "2", 0, None, "1/3 + 1/6 = 1/2. Reciprocal is 2.", "\\(\\frac{1}{1/2} = 2\\)."),
        q("ex10-q3", 10, "mental", "Mental Arithmetic", "numeric", "Calculate: \\( 16\\% \\) of \\( 625 \\)", 100, "100", 0, None, "6.25 * 16 = 100.", "\\(0.16 \\times 625 = 100\\)."),
        # 2. Fractions & Decimals
        q("ex10-q4", 10, "fractions", "Fractions & Decimals", "numeric", "Evaluate: \\( \\frac{1}{4} + \\frac{1}{6} + \\frac{1}{12} \\)", 0.5, "0.5 (or 1/2)", 0.01, None, "(3 + 2 + 1)/12 = 6/12 = 0.5.", "\\(\\frac{6}{12} = 0.5\\)."),
        q("ex10-q5", 10, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 5.5^2 \\)", 30.25, "30.25", 0.01, None, "5 * 6 = 30 => 30.25.", "\\(5.5^2 = 30.25\\)."),
        q("ex10-q6", 10, "fractions", "Fractions & Decimals", "numeric", "Calculate: \\( 3.6 \\times 0.25 \\times 8 \\)", 7.2, "7.2", 0.01, None, "0.25 * 8 = 2. 3.6 * 2 = 7.2.", "\\(3.6 \\times 2 = 7.2\\)."),
        # 3. Powers, Roots & Surds
        q("ex10-q7", 10, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 26^2 \\)", 676, "676", 0, None, "26 * 26 = 676.", "\\(26^2 = 676\\)."),
        q("ex10-q8", 10, "powers", "Powers, Roots & Surds", "numeric", "Calculate: \\( 27^2 \\)", 729, "729", 0, None, "27 * 27 = 729.", "\\(27^2 = 729\\)."),
        q("ex10-q9", 10, "powers", "Powers, Roots & Surds", "numeric", "Evaluate: \\( \\sqrt{50} \\div \\sqrt{2} \\)", 5, "5", 0, None, "sqrt(50 / 2) = sqrt(25) = 5.", "\\(\\sqrt{25} = 5\\)."),
        # 4. Algebra & Equations
        q("ex10-q10", 10, "algebra", "Algebra & Equations", "numeric", "If \\( a + b = 9 \\) and \\( ab = 20 \\), find \\( a^2 + b^2 \\).", 41, "41", 0, None, "(a + b)^2 - 2ab = 81 - 40 = 41.", "\\(81 - 40 = 41\\)."),
        q("ex10-q11", 10, "algebra", "Algebra & Equations", "numeric", "Solve for positive \\( x \\): \\( \\sqrt{2x + 7} = 5 \\)", 9, "9", 0, None, "2x + 7 = 25 => 2x = 18 => x = 9.", "\\(2x = 18 \\implies x = 9\\)."),
        q("ex10-q12", 10, "algebra", "Algebra & Equations", "numeric", "Solve the system for \\( x \\): \\( 3x + 2y = 19 \\) and \\( 2x - y = 8 \\).", 5, "5", 0, None, "Multiply 2nd eq by 2: 4x - 2y = 16. Add: 7x = 35 => x = 5.", "\\(7x = 35 \\implies x = 5\\)."),
        # 5. Scientific Notation & Estimation
        q("ex10-q13", 10, "scientific", "Scientific Notation & Estimation", "numeric", "Evaluate: \\( \\frac{2 \\times 10^{-7} \\times 10}{10^{-6}} \\)", 2, "2", 0.01, None, "2 * 10^(-6) / 10^(-6) = 2.", "\\(2 \\times 10^0 = 2\\)."),
        q("ex10-q14", 10, "scientific", "Scientific Notation & Estimation", "numeric", "Calculate: \\( 2.4 \\times 10^3 \\div (8 \\times 10^{-2}) \\)", 30000, "30,000 (or 3×10⁴)", 1, None, "0.3 * 10^5 = 30000.", "\\(0.3 \\times 10^5 = 30,000\\)."),
        q("ex10-q15", 10, "scientific", "Scientific Notation & Estimation", "numeric", "Simplify: \\( \\sqrt{108} \\div \\sqrt{3} \\)", 6, "6", 0, None, "sqrt(108 / 3) = sqrt(36) = 6.", "\\(\\sqrt{36} = 6\\).")
    ]
})

print(f"Days 1-10 created: {len(days_1_10)} exercises.")
