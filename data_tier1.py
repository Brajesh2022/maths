# Tier 1: Exercises 1 - 5 (Foundation)

tier1 = [
    {
        "id": 1,
        "title": "Foundation: Basic Operations & Substitution",
        "subtitle": "Rebuild mental arithmetic speed, basic algebra, and simple formula substitutions.",
        "difficulty": 1,
        "tier": "Foundation",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex1-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 17 \\times 6 \\)",
                "answer": 102, "displayAnswer": "102", "tolerance": 0, "unit": "",
                "hint": "Split 17 as (10 + 7) and multiply each by 6.",
                "explanation": "\\(17 \\times 6 = (10 \\times 6) + (7 \\times 6) = 60 + 42 = 102\\)."
            },
            {
                "id": "ex1-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 144 \\div 12 \\)",
                "answer": 12, "displayAnswer": "12", "tolerance": 0, "unit": "",
                "hint": "Recall 12 squared.",
                "explanation": "\\(12 \\times 12 = 144\\), so \\(144 \\div 12 = 12\\)."
            },
            {
                "id": "ex1-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate \\( 25\\% \\) of \\( 240 \\)",
                "answer": 60, "displayAnswer": "60", "tolerance": 0, "unit": "",
                "hint": "25% is equivalent to dividing by 4.",
                "explanation": "\\(25\\% = \\frac{1}{4}\\). \\(240 \\div 4 = 60\\)."
            },
            {
                "id": "ex1-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 3.5 + 2.75 \\)",
                "answer": 6.25, "displayAnswer": "6.25", "tolerance": 0.01, "unit": "",
                "hint": "Add whole numbers first: 3 + 2 = 5, then 0.50 + 0.75.",
                "explanation": "\\(3.50 + 2.75 = 5.00 + 1.25 = 6.25\\)."
            },
            {
                "id": "ex1-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 0.8 \\times 0.25 \\)",
                "answer": 0.2, "displayAnswer": "0.2", "tolerance": 0.01, "unit": "",
                "hint": "0.25 is 1/4. So take one-fourth of 0.8.",
                "explanation": "\\(0.8 \\times 0.25 = 0.8 \\times \\frac{1}{4} = 0.2\\)."
            },
            # Algebra (5)
            {
                "id": "ex1-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify the fraction \\( \\frac{18}{24} \\) to lowest terms. Express as a decimal.",
                "answer": 0.75, "displayAnswer": "0.75 (or 3/4)", "tolerance": 0.01, "unit": "",
                "hint": "Divide numerator and denominator by their GCD (6).",
                "explanation": "\\(\\frac{18}{24} = \\frac{18 \\div 6}{24 \\div 6} = \\frac{3}{4} = 0.75\\)."
            },
            {
                "id": "ex1-q7", "section": "algebra", "sectionName": "Algebra", "type": "mcq",
                "question": "Which of the following is the correct algebraic expansion of \\( (a+b)^2 \\)?",
                "options": ["\\( a^2 + b^2 \\)", "\\( a^2 + 2ab + b^2 \\)", "\\( a^2 - 2ab + b^2 \\)", "\\( 2a + 2b \\)"],
                "answer": 1, "displayAnswer": "a² + 2ab + b²", "tolerance": 0, "unit": "",
                "hint": "Remember the middle cross-term from FOIL: a*b + b*a = 2ab.",
                "explanation": "\\((a+b)^2 = (a+b)(a+b) = a^2 + ab + ba + b^2 = a^2 + 2ab + b^2\\)."
            },
            {
                "id": "ex1-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the positive root of the quadratic equation: \\( x^2 - 5x + 6 = 0 \\)",
                "answer": 3, "displayAnswer": "3 (roots are 2, 3)", "tolerance": 0.01, "unit": "",
                "hint": "Factor into (x - 2)(x - 3) = 0.",
                "explanation": "\\(x^2 - 5x + 6 = (x-2)(x-3) = 0\\). The roots are \\(x = 2\\) and \\(x = 3\\). Either 2 or 3 is correct (larger root is 3)."
            },
            {
                "id": "ex1-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Rearrange \\( y = 3x - 6 \\). If \\( y = 12 \\), what is the value of \\( x \\)?",
                "answer": 6, "displayAnswer": "6", "tolerance": 0, "unit": "",
                "hint": "Add 6 to both sides, then divide by 3.",
                "explanation": "\\(12 = 3x - 6 \\implies 3x = 18 \\implies x = 6\\)."
            },
            {
                "id": "ex1-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( 3(2x + 4) - 2(x - 1) \\). What is the value when \\( x = 2 \\)?",
                "answer": 22, "displayAnswer": "22", "tolerance": 0, "unit": "",
                "hint": "Expand: 6x + 12 - 2x + 2 = 4x + 14.",
                "explanation": "\\(3(2x+4) - 2(x-1) = 6x + 12 - 2x + 2 = 4x + 14\\). At \\(x = 2\\): \\(4(2) + 14 = 8 + 14 = 22\\)."
            },
            # Physics-Style Calculations (5)
            {
                "id": "ex1-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 14^2 \\)",
                "answer": 196, "displayAnswer": "196", "tolerance": 0, "unit": "",
                "hint": "14 * 14 = 14 * 10 + 14 * 4.",
                "explanation": "\\(14^2 = 196\\). Memorize squares up to 30 for NEET/JEE speed."
            },
            {
                "id": "ex1-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert the fraction \\( \\frac{3}{8} \\) to its decimal equivalent.",
                "answer": 0.375, "displayAnswer": "0.375", "tolerance": 0.005, "unit": "",
                "hint": "1/8 = 0.125. Multiply 0.125 by 3.",
                "explanation": "\\(\\frac{1}{8} = 0.125\\), so \\(\\frac{3}{8} = 3 \\times 0.125 = 0.375\\)."
            },
            {
                "id": "ex1-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate powers of 10: \\( \\frac{10^5 \\times 10^{-2}}{10^1} \\)",
                "answer": 100, "displayAnswer": "100 (or 10²)", "tolerance": 0.01, "unit": "",
                "hint": "Add exponents in the numerator, then subtract exponent in the denominator.",
                "explanation": "\\(10^{5 + (-2) - 1} = 10^2 = 100\\)."
            },
            {
                "id": "ex1-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the standard approximation of \\( \\sqrt{3} \\) to 2 decimal places?",
                "answer": 1.73, "displayAnswer": "1.73", "tolerance": 0.02, "unit": "",
                "hint": "Between 1.7 and 1.8.",
                "explanation": "\\(\\sqrt{3} \\approx 1.732\\). In NEET/JEE numericals, 1.73 is standard."
            },
            {
                "id": "ex1-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A particle moves with uniform speed and covers distance \\( s = 120 \\text{ m} \\) in time \\( t = 6 \\text{ s} \\). Using \\( v = \\frac{s}{t} \\), find \\( v \\) in \\( \\text{m/s} \\).",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "m/s",
                "hint": "Divide distance by time: 120 / 6.",
                "explanation": "\\(v = \\frac{s}{t} = \\frac{120}{6} = 20 \\text{ m/s}\\)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Foundation: Decimal Fluency & Linear Equations",
        "subtitle": "Master two-digit multiplication, decimal operations, linear equations, and force calculations.",
        "difficulty": 1,
        "tier": "Foundation",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex2-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 19 \\times 7 \\)",
                "answer": 133, "displayAnswer": "133", "tolerance": 0, "unit": "",
                "hint": "Use (20 - 1) * 7 = 140 - 7.",
                "explanation": "\\(19 \\times 7 = (20 - 1) \\times 7 = 140 - 7 = 133\\)."
            },
            {
                "id": "ex2-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 225 \\div 15 \\)",
                "answer": 15, "displayAnswer": "15", "tolerance": 0, "unit": "",
                "hint": "15 squared is 225.",
                "explanation": "\\(15 \\times 15 = 225\\), therefore \\(225 \\div 15 = 15\\)."
            },
            {
                "id": "ex2-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate \\( 15\\% \\) of \\( 320 \\)",
                "answer": 48, "displayAnswer": "48", "tolerance": 0, "unit": "",
                "hint": "10% of 320 is 32; 5% is 16. Add them.",
                "explanation": "\\(10\\% = 32\\), \\(5\\% = 16\\). \\(32 + 16 = 48\\)."
            },
            {
                "id": "ex2-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 7.6 - 3.85 \\)",
                "answer": 3.75, "displayAnswer": "3.75", "tolerance": 0.01, "unit": "",
                "hint": "7.60 - 3.85 = 7.60 - 3.80 - 0.05.",
                "explanation": "\\(7.60 - 3.85 = 3.75\\)."
            },
            {
                "id": "ex2-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 1.2 \\times 0.5 \\)",
                "answer": 0.6, "displayAnswer": "0.6", "tolerance": 0.01, "unit": "",
                "hint": "Multiplying by 0.5 is taking half.",
                "explanation": "\\(1.2 \\times 0.5 = 1.2 \\div 2 = 0.6\\)."
            },
            # Algebra (5)
            {
                "id": "ex2-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 4x - 7 = 21 \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "Add 7 to both sides, then divide by 4.",
                "explanation": "\\(4x = 28 \\implies x = 7\\)."
            },
            {
                "id": "ex2-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate \\( (x - 3)^2 \\) when \\( x = 8 \\).",
                "answer": 25, "displayAnswer": "25", "tolerance": 0, "unit": "",
                "hint": "Compute (8 - 3) first, then square.",
                "explanation": "\\((8 - 3)^2 = 5^2 = 25\\)."
            },
            {
                "id": "ex2-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for the positive value of \\( x \\): \\( x^2 - 9 = 0 \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "x² = 9.",
                "explanation": "\\(x^2 = 9 \\implies x = \\pm 3\\). Positive value is 3."
            },
            {
                "id": "ex2-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{x}{5} + 3 = 11 \\)",
                "answer": 40, "displayAnswer": "40", "tolerance": 0, "unit": "",
                "hint": "Subtract 3 first: x/5 = 8, then multiply by 5.",
                "explanation": "\\(\\frac{x}{5} = 8 \\implies x = 8 \\times 5 = 40\\)."
            },
            {
                "id": "ex2-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify the fraction \\( \\frac{45}{60} \\) to its decimal form.",
                "answer": 0.75, "displayAnswer": "0.75 (or 3/4)", "tolerance": 0.01, "unit": "",
                "hint": "Divide both by 15.",
                "explanation": "\\(\\frac{45}{60} = \\frac{3}{4} = 0.75\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex2-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 16^2 \\)",
                "answer": 256, "displayAnswer": "256", "tolerance": 0, "unit": "",
                "hint": "16 * 16 = 256.",
                "explanation": "\\(16^2 = 256\\)."
            },
            {
                "id": "ex2-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is \\( 0.625 \\) expressed as a simplified fraction \\( \\frac{a}{b} \\)? What is the denominator \\( b \\)?",
                "answer": 8, "displayAnswer": "8 (Fraction is 5/8)", "tolerance": 0, "unit": "",
                "hint": "0.625 = 5 * 0.125 = 5/8.",
                "explanation": "\\(0.625 = \\frac{625}{1000} = \\frac{5}{8}\\). The denominator is 8."
            },
            {
                "id": "ex2-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the standard approximation of \\( \\sqrt{2} \\) to 2 decimal places?",
                "answer": 1.41, "displayAnswer": "1.41 (or 1.414)", "tolerance": 0.02, "unit": "",
                "hint": "Approx 1.414.",
                "explanation": "\\(\\sqrt{2} \\approx 1.414\\). Used in AC peak voltage \\(V_0 = \\sqrt{2}V_{rms}\\)."
            },
            {
                "id": "ex2-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{10^7 \\times 10^{-3}}{10^2} \\)",
                "answer": 100, "displayAnswer": "100 (or 10²)", "tolerance": 0.01, "unit": "",
                "hint": "7 - 3 - 2 = 2.",
                "explanation": "\\(10^{7 - 3 - 2} = 10^2 = 100\\)."
            },
            {
                "id": "ex2-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Using Newton's Second Law \\( F = ma \\), find force \\( F \\) when mass \\( m = 5 \\text{ kg} \\) and acceleration \\( a = 4 \\text{ m/s}^2 \\).",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "N",
                "hint": "Multiply mass by acceleration: 5 * 4.",
                "explanation": "\\(F = ma = 5 \\times 4 = 20 \\text{ N}\\)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Foundation: Percentages & Square Fluency",
        "subtitle": "Build speed with percentages, quadratic factorization, and work calculations.",
        "difficulty": 1,
        "tier": "Foundation",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex3-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 23 \\times 4 \\)",
                "answer": 92, "displayAnswer": "92", "tolerance": 0, "unit": "",
                "hint": "20 * 4 + 3 * 4 = 80 + 12.",
                "explanation": "\\(23 \\times 4 = 80 + 12 = 92\\)."
            },
            {
                "id": "ex3-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 196 \\div 14 \\)",
                "answer": 14, "displayAnswer": "14", "tolerance": 0, "unit": "",
                "hint": "14 squared is 196.",
                "explanation": "\\(196 \\div 14 = 14\\)."
            },
            {
                "id": "ex3-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate \\( 30\\% \\) of \\( 450 \\)",
                "answer": 135, "displayAnswer": "135", "tolerance": 0, "unit": "",
                "hint": "10% is 45. Multiply 45 by 3.",
                "explanation": "\\(3 \\times 45 = 135\\)."
            },
            {
                "id": "ex3-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 4.25 + 6.85 \\)",
                "answer": 11.1, "displayAnswer": "11.1", "tolerance": 0.01, "unit": "",
                "hint": "4 + 6 = 10; 0.25 + 0.85 = 1.10.",
                "explanation": "\\(4.25 + 6.85 = 11.10\\)."
            },
            {
                "id": "ex3-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 0.6 \\times 0.15 \\)",
                "answer": 0.09, "displayAnswer": "0.09", "tolerance": 0.005, "unit": "",
                "hint": "6 * 15 = 90. Shift decimal 3 places.",
                "explanation": "\\(0.6 \\times 0.15 = 0.090 = 0.09\\)."
            },
            # Algebra (5)
            {
                "id": "ex3-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 5x + 9 = 44 \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "5x = 44 - 9 = 35.",
                "explanation": "\\(5x = 35 \\implies x = 7\\)."
            },
            {
                "id": "ex3-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate \\( (2x + 1)^2 \\) when \\( x = 3 \\).",
                "answer": 49, "displayAnswer": "49", "tolerance": 0, "unit": "",
                "hint": "2(3) + 1 = 7. Then 7 squared.",
                "explanation": "\\((2 \\times 3 + 1)^2 = 7^2 = 49\\)."
            },
            {
                "id": "ex3-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the smaller root of \\( x^2 - 7x + 12 = 0 \\).",
                "answer": 3, "displayAnswer": "3 (roots are 3, 4)", "tolerance": 0, "unit": "",
                "hint": "Factor into (x - 3)(x - 4) = 0.",
                "explanation": "\\((x-3)(x-4) = 0\\). Roots are 3 and 4. Smaller root is 3."
            },
            {
                "id": "ex3-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 2(x - 4) = 16 \\)",
                "answer": 12, "displayAnswer": "12", "tolerance": 0, "unit": "",
                "hint": "Divide by 2: x - 4 = 8.",
                "explanation": "\\(x - 4 = 8 \\implies x = 12\\)."
            },
            {
                "id": "ex3-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{36}{84} \\) to lowest terms. Enter decimal value to 3 decimal places.",
                "answer": 0.429, "displayAnswer": "0.429 (or 3/7)", "tolerance": 0.01, "unit": "",
                "hint": "Divide numerator and denominator by 12.",
                "explanation": "\\(\\frac{36}{84} = \\frac{3}{7} \\approx 0.4286 \\approx 0.429\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex3-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 17^2 \\)",
                "answer": 289, "displayAnswer": "289", "tolerance": 0, "unit": "",
                "hint": "17 * 17.",
                "explanation": "\\(17^2 = 289\\)."
            },
            {
                "id": "ex3-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert \\( \\frac{7}{20} \\) to its decimal equivalent.",
                "answer": 0.35, "displayAnswer": "0.35", "tolerance": 0.005, "unit": "",
                "hint": "Multiply numerator and denominator by 5: 35/100.",
                "explanation": "\\(\\frac{7 \\times 5}{20 \\times 5} = \\frac{35}{100} = 0.35\\)."
            },
            {
                "id": "ex3-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the standard approximation of \\( \\sqrt{5} \\) to 2 decimal places?",
                "answer": 2.24, "displayAnswer": "2.24", "tolerance": 0.02, "unit": "",
                "hint": "2.24 * 2.24 = 5.0176.",
                "explanation": "\\(\\sqrt{5} \\approx 2.236 \\approx 2.24\\)."
            },
            {
                "id": "ex3-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( 10^6 \\times 10^{-4} \\)",
                "answer": 100, "displayAnswer": "100 (or 10²)", "tolerance": 0, "unit": "",
                "hint": "6 + (-4) = 2.",
                "explanation": "\\(10^2 = 100\\)."
            },
            {
                "id": "ex3-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A force of \\( F = 15 \\text{ N} \\) moves a block through displacement \\( s = 8 \\text{ m} \\) in the direction of the force. Using \\( W = Fs \\), calculate the work done \\( W \\) in Joules.",
                "answer": 120, "displayAnswer": "120", "tolerance": 0, "unit": "J",
                "hint": "15 * 8 = 15 * 2 * 4 = 30 * 4.",
                "explanation": "\\(W = F \\times s = 15 \\times 8 = 120 \\text{ J}\\)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Foundation: Powers of Ten & Power Formulas",
        "subtitle": "Master fractional simplification, powers of ten, and electric/mechanical power calculations.",
        "difficulty": 1,
        "tier": "Foundation",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex4-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 16 \\times 8 \\)",
                "answer": 128, "displayAnswer": "128", "tolerance": 0, "unit": "",
                "hint": "2^4 * 2^3 = 2^7 = 128.",
                "explanation": "\\(16 \\times 8 = 128\\)."
            },
            {
                "id": "ex4-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 169 \\div 13 \\)",
                "answer": 13, "displayAnswer": "13", "tolerance": 0, "unit": "",
                "hint": "13 squared is 169.",
                "explanation": "\\(169 \\div 13 = 13\\)."
            },
            {
                "id": "ex4-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate \\( 12.5\\% \\) of \\( 160 \\)",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "",
                "hint": "12.5% is 1/8. Divide 160 by 8.",
                "explanation": "\\(160 \\div 8 = 20\\)."
            },
            {
                "id": "ex4-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 9.1 - 4.45 \\)",
                "answer": 4.65, "displayAnswer": "4.65", "tolerance": 0.01, "unit": "",
                "hint": "9.10 - 4.45.",
                "explanation": "\\(9.10 - 4.45 = 4.65\\)."
            },
            {
                "id": "ex4-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 1.5 \\times 0.04 \\)",
                "answer": 0.06, "displayAnswer": "0.06", "tolerance": 0.005, "unit": "",
                "hint": "15 * 4 = 60. Shift 3 decimal places.",
                "explanation": "\\(1.5 \\times 0.04 = 0.060 = 0.06\\)."
            },
            # Algebra (5)
            {
                "id": "ex4-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 7x - 15 = 34 \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "7x = 34 + 15 = 49.",
                "explanation": "\\(7x = 49 \\implies x = 7\\)."
            },
            {
                "id": "ex4-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( x^2 - 16 = 0 \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "Square root of 16.",
                "explanation": "\\(x = 4\\)."
            },
            {
                "id": "ex4-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{x^2 - 4}{x - 2} \\). Evaluate at \\( x = 5 \\).",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "(x^2 - 4) = (x - 2)(x + 2). So it reduces to (x + 2).",
                "explanation": "\\(\\frac{(x-2)(x+2)}{x-2} = x + 2\\). At \\(x = 5\\), \\(5 + 2 = 7\\)."
            },
            {
                "id": "ex4-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{2x + 6}{4} = 5 \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "Multiply both sides by 4: 2x + 6 = 20.",
                "explanation": "\\(2x + 6 = 20 \\implies 2x = 14 \\implies x = 7\\)."
            },
            {
                "id": "ex4-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{54}{90} \\) to its decimal value.",
                "answer": 0.6, "displayAnswer": "0.6 (or 3/5)", "tolerance": 0.01, "unit": "",
                "hint": "Divide numerator and denominator by 18.",
                "explanation": "\\(\\frac{54}{90} = \\frac{3}{5} = 0.6\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex4-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 18^2 \\)",
                "answer": 324, "displayAnswer": "324", "tolerance": 0, "unit": "",
                "hint": "18 * 18.",
                "explanation": "\\(18^2 = 324\\)."
            },
            {
                "id": "ex4-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert \\( \\frac{5}{16} \\) to its decimal value.",
                "answer": 0.3125, "displayAnswer": "0.3125", "tolerance": 0.005, "unit": "",
                "hint": "1/16 = 0.0625. Multiply by 5.",
                "explanation": "\\(5 \\times 0.0625 = 0.3125\\)."
            },
            {
                "id": "ex4-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( 10^{-3} \\times 10^7 \\)",
                "answer": 10000, "displayAnswer": "10000 (or 10⁴)", "tolerance": 0.01, "unit": "",
                "hint": "-3 + 7 = 4.",
                "explanation": "\\(10^4 = 10,000\\)."
            },
            {
                "id": "ex4-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the standard approximation of \\( \\sqrt{10} \\) to 2 decimal places? (Recall: \\( \\pi^2 \\approx 10 \\))",
                "answer": 3.16, "displayAnswer": "3.16", "tolerance": 0.02, "unit": "",
                "hint": "Very close to pi (3.1416). Actually 3.162.",
                "explanation": "\\(\\sqrt{10} \\approx 3.162\\). Often rounded to 3.16."
            },
            {
                "id": "ex4-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A machine performs work \\( W = 360 \\text{ J} \\) in time \\( t = 12 \\text{ s} \\). Using \\( P = \\frac{W}{t} \\), find the power \\( P \\) in Watts.",
                "answer": 30, "displayAnswer": "30", "tolerance": 0, "unit": "W",
                "hint": "Divide 360 by 12.",
                "explanation": "\\(P = \\frac{W}{t} = \\frac{360}{12} = 30 \\text{ W}\\)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Foundation: Ohm's Law & Scientific Notation",
        "subtitle": "Master fractions, scientific notation product, and Ohm's law substitutions.",
        "difficulty": 1,
        "tier": "Foundation",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex5-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 24 \\times 5 \\)",
                "answer": 120, "displayAnswer": "120", "tolerance": 0, "unit": "",
                "hint": "Divide 24 by 2 and add zero: 12 -> 120.",
                "explanation": "\\(24 \\times 5 = 120\\)."
            },
            {
                "id": "ex5-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 256 \\div 16 \\)",
                "answer": 16, "displayAnswer": "16", "tolerance": 0, "unit": "",
                "hint": "16 squared is 256.",
                "explanation": "\\(256 \\div 16 = 16\\)."
            },
            {
                "id": "ex5-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate \\( 40\\% \\) of \\( 350 \\)",
                "answer": 140, "displayAnswer": "140", "tolerance": 0, "unit": "",
                "hint": "10% is 35. Multiply 35 by 4.",
                "explanation": "\\(35 \\times 4 = 140\\)."
            },
            {
                "id": "ex5-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 5.35 + 8.75 \\)",
                "answer": 14.1, "displayAnswer": "14.1", "tolerance": 0.01, "unit": "",
                "hint": "5 + 8 = 13; 0.35 + 0.75 = 1.10.",
                "explanation": "\\(13 + 1.10 = 14.1\\)."
            },
            {
                "id": "ex5-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 0.75 \\times 0.8 \\)",
                "answer": 0.6, "displayAnswer": "0.6", "tolerance": 0.01, "unit": "",
                "hint": "3/4 of 0.8 = 0.6.",
                "explanation": "\\(\\frac{3}{4} \\times 0.8 = 3 \\times 0.2 = 0.6\\)."
            },
            # Algebra (5)
            {
                "id": "ex5-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 3(x + 4) = 27 \\)",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "x + 4 = 9.",
                "explanation": "\\(x = 9 - 4 = 5\\)."
            },
            {
                "id": "ex5-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate \\( (x + 5)(x - 5) \\) when \\( x = 7 \\).",
                "answer": 24, "displayAnswer": "24", "tolerance": 0, "unit": "",
                "hint": "(x+5)(x-5) = x^2 - 25 = 49 - 25.",
                "explanation": "\\(7^2 - 25 = 49 - 25 = 24\\)."
            },
            {
                "id": "ex5-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the larger root of \\( x^2 - 8x + 15 = 0 \\).",
                "answer": 5, "displayAnswer": "5 (roots are 3, 5)", "tolerance": 0, "unit": "",
                "hint": "Factor: (x - 3)(x - 5) = 0.",
                "explanation": "\\((x-3)(x-5) = 0\\). The larger root is 5."
            },
            {
                "id": "ex5-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Rearrange \\( v = u + at \\) for acceleration \\( a \\). If \\( v = 20 \\), \\( u = 5 \\), and \\( t = 3 \\), find \\( a \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "a = (v - u) / t = (20 - 5) / 3.",
                "explanation": "\\(a = \\frac{20 - 5}{3} = \\frac{15}{3} = 5\\)."
            },
            {
                "id": "ex5-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{48}{72} \\) to lowest terms. Express as a decimal.",
                "answer": 0.667, "displayAnswer": "0.667 (or 2/3)", "tolerance": 0.01, "unit": "",
                "hint": "Divide both by 24.",
                "explanation": "\\(\\frac{48}{72} = \\frac{2}{3} \\approx 0.667\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex5-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 19^2 \\)",
                "answer": 361, "displayAnswer": "361", "tolerance": 0, "unit": "",
                "hint": "(20 - 1)^2 = 400 - 40 + 1 = 361.",
                "explanation": "\\(19^2 = 361\\)."
            },
            {
                "id": "ex5-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert \\( \\frac{9}{25} \\) to its decimal equivalent.",
                "answer": 0.36, "displayAnswer": "0.36", "tolerance": 0.005, "unit": "",
                "hint": "Multiply numerator and denominator by 4.",
                "explanation": "\\(\\frac{9 \\times 4}{25 \\times 4} = \\frac{36}{100} = 0.36\\)."
            },
            {
                "id": "ex5-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{10^8}{10^5} \\)",
                "answer": 1000, "displayAnswer": "1000 (or 10³)", "tolerance": 0, "unit": "",
                "hint": "8 - 5 = 3.",
                "explanation": "\\(10^{8-5} = 10^3 = 1000\\)."
            },
            {
                "id": "ex5-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the product in standard form: \\( (2 \\times 10^3) \\times (3 \\times 10^2) \\). Enter numerical value.",
                "answer": 600000, "displayAnswer": "600,000 (or 6×10⁵)", "tolerance": 1, "unit": "",
                "hint": "(2 * 3) * 10^(3 + 2) = 6 * 10^5.",
                "explanation": "\\(6 \\times 10^5 = 600,000\\)."
            },
            {
                "id": "ex5-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A resistor of \\( R = 8 \\text{ }\\Omega \\) carries a steady current \\( I = 2.5 \\text{ A} \\). Using Ohm's Law \\( V = IR \\), find the voltage \\( V \\) in Volts.",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "V",
                "hint": "2.5 * 8 = (5/2) * 8 = 20.",
                "explanation": "\\(V = 2.5 \\times 8 = 20 \\text{ V}\\)."
            }
        ]
    }
]

print(f"Tier 1 loaded: {len(tier1)} exercises.")
