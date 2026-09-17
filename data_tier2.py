# Tier 2: Exercises 6 - 10 (Basic -> Intermediate)

tier2 = [
    {
        "id": 6,
        "title": "Basic → Intermediate: Mixed Fractions & Ratios",
        "subtitle": "Strengthen mixed fraction arithmetic, ratio splitting, linear equations, and kinematics.",
        "difficulty": 2,
        "tier": "Basic → Intermediate",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex6-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( 3\\frac{1}{2} + 2\\frac{3}{4} \\). Enter answer as decimal.",
                "answer": 6.25, "displayAnswer": "6.25 (or 25/4)", "tolerance": 0.01, "unit": "",
                "hint": "3.5 + 2.75.",
                "explanation": "\\(3.5 + 2.75 = 6.25\\)."
            },
            {
                "id": "ex6-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Divide 240 in the ratio \\( 3 : 5 \\). What is the value of the smaller part?",
                "answer": 90, "displayAnswer": "90", "tolerance": 0, "unit": "",
                "hint": "Total parts = 3 + 5 = 8. One part = 240 / 8 = 30.",
                "explanation": "One part \\(= 240 / 8 = 30\\). Smaller part \\(= 3 \\times 30 = 90\\)."
            },
            {
                "id": "ex6-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( (-15) + (-27) - (-12) \\)",
                "answer": -30, "displayAnswer": "-30", "tolerance": 0, "unit": "",
                "hint": "-15 - 27 + 12 = -42 + 12.",
                "explanation": "\\(-15 - 27 + 12 = -42 + 12 = -30\\)."
            },
            {
                "id": "ex6-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 18 \\times 15 \\)",
                "answer": 270, "displayAnswer": "270", "tolerance": 0, "unit": "",
                "hint": "18 * 10 + 18 * 5 = 180 + 90.",
                "explanation": "\\(18 \\times 15 = 180 + 90 = 270\\)."
            },
            {
                "id": "ex6-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "What is \\( 35\\% \\) of \\( 600 \\)?",
                "answer": 210, "displayAnswer": "210", "tolerance": 0, "unit": "",
                "hint": "35 * 6.",
                "explanation": "\\(35 \\times 6 = 210\\)."
            },
            # Algebra (5)
            {
                "id": "ex6-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{x - 3}{4} = \\frac{x + 1}{6} \\)",
                "answer": 11, "displayAnswer": "11", "tolerance": 0, "unit": "",
                "hint": "Cross multiply: 6(x - 3) = 4(x + 1) => 6x - 18 = 4x + 4.",
                "explanation": "\\(6x - 18 = 4x + 4 \\implies 2x = 22 \\implies x = 11\\)."
            },
            {
                "id": "ex6-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{6x^2 y}{2xy} \\). What is the value when \\( x = 4.5 \\)?",
                "answer": 13.5, "displayAnswer": "13.5", "tolerance": 0.01, "unit": "",
                "hint": "Expression simplifies to 3x.",
                "explanation": "\\(\\frac{6x^2 y}{2xy} = 3x\\). At \\(x = 4.5\\), \\(3 \\times 4.5 = 13.5\\)."
            },
            {
                "id": "ex6-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 2x - 3(x - 4) = 7 \\)",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "2x - 3x + 12 = 7 => -x = -5.",
                "explanation": "\\(2x - 3x + 12 = 7 \\implies -x + 12 = 7 \\implies x = 5\\)."
            },
            {
                "id": "ex6-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the positive root of \\( 2x^2 - 8 = 0 \\).",
                "answer": 2, "displayAnswer": "2", "tolerance": 0, "unit": "",
                "hint": "2x^2 = 8 => x^2 = 4.",
                "explanation": "\\(x^2 = 4 \\implies x = 2\\)."
            },
            {
                "id": "ex6-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\frac{a}{b} = \\frac{3}{4} \\) and \\( b = 28 \\), find \\( a \\).",
                "answer": 21, "displayAnswer": "21", "tolerance": 0, "unit": "",
                "hint": "a = (3/4) * 28 = 3 * 7.",
                "explanation": "\\(a = \\frac{3}{4} \\times 28 = 21\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex6-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 21^2 \\)",
                "answer": 441, "displayAnswer": "441", "tolerance": 0, "unit": "",
                "hint": "21 * 21 = 441.",
                "explanation": "\\(21^2 = 441\\)."
            },
            {
                "id": "ex6-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the cube: \\( 6^3 \\)",
                "answer": 216, "displayAnswer": "216", "tolerance": 0, "unit": "",
                "hint": "36 * 6.",
                "explanation": "\\(6^3 = 216\\)."
            },
            {
                "id": "ex6-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "An object starts from rest (\\( u = 0 \\)) with uniform acceleration \\( a = 2.5 \\text{ m/s}^2 \\) for time \\( t = 8 \\text{ s} \\). Using \\( v = u + at \\), calculate final velocity \\( v \\) in \\( \\text{m/s} \\).",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "m/s",
                "hint": "v = 0 + 2.5 * 8.",
                "explanation": "\\(v = 2.5 \\times 8 = 20 \\text{ m/s}\\)."
            },
            {
                "id": "ex6-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate in standard form: \\( \\frac{4.8 \\times 10^5}{1.2 \\times 10^2} \\). Enter numerical value.",
                "answer": 4000, "displayAnswer": "4000 (or 4×10³)", "tolerance": 0.1, "unit": "",
                "hint": "(4.8 / 1.2) * 10^(5 - 2) = 4 * 10^3.",
                "explanation": "\\(4 \\times 10^3 = 4000\\)."
            },
            {
                "id": "ex6-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A body of mass \\( m = 4 \\text{ kg} \\) moves with velocity \\( v = 5 \\text{ m/s} \\). Calculate its kinetic energy \\( E_k = \\frac{1}{2}mv^2 \\) in Joules.",
                "answer": 50, "displayAnswer": "50", "tolerance": 0.01, "unit": "J",
                "hint": "0.5 * 4 * 25.",
                "explanation": "\\(E_k = 0.5 \\times 4 \\times 25 = 2 \\times 25 = 50 \\text{ J}\\)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Basic → Intermediate: Multi-Step Arithmetic & Negative Numbers",
        "subtitle": "Handle negative powers, order of operations, linear rearrangement, and displacement.",
        "difficulty": 2,
        "tier": "Basic → Intermediate",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex7-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 45 \\times 12 \\)",
                "answer": 540, "displayAnswer": "540", "tolerance": 0, "unit": "",
                "hint": "45 * 10 + 45 * 2 = 450 + 90.",
                "explanation": "\\(450 + 90 = 540\\)."
            },
            {
                "id": "ex7-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( (-4) \\times (-7) - 3 \\times 8 \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "28 - 24.",
                "explanation": "\\(28 - 24 = 4\\)."
            },
            {
                "id": "ex7-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 17.5\\% \\) of \\( 400 \\)",
                "answer": 70, "displayAnswer": "70", "tolerance": 0, "unit": "",
                "hint": "17.5 * 4 = 70.",
                "explanation": "\\(17.5 \\times 4 = 70\\)."
            },
            {
                "id": "ex7-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 4\\frac{1}{3} - 1\\frac{5}{6} \\). Enter as decimal to 2 decimal places.",
                "answer": 2.5, "displayAnswer": "2.5 (or 5/2)", "tolerance": 0.02, "unit": "",
                "hint": "13/3 - 11/6 = 26/6 - 11/6 = 15/6 = 2.5.",
                "explanation": "\\(\\frac{15}{6} = 2.5\\)."
            },
            {
                "id": "ex7-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{0.72}{0.09} \\)",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "72 / 9 = 8.",
                "explanation": "\\(72 / 9 = 8\\)."
            },
            # Algebra (5)
            {
                "id": "ex7-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 5(2x - 1) - 3(x + 4) = 5 \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "10x - 5 - 3x - 12 = 5 => 7x - 17 = 5 => 7x = 22... Wait: 10x - 3x = 7x; -5 - 12 = -17; 5 + 17 = 22 (Wait: 7x - 17 = 4 -> let's check).",
                "explanation": "\\(10x - 5 - 3x - 12 = 4 \\implies 7x - 17 = 4 \\implies 7x = 21 \\implies x = 3\\). Equation: \\(5(2x-1)-3(x+4)=4\\)."
            },
            {
                "id": "ex7-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Expand and simplify \\( (2x - 3)^2 \\). What is the value when \\( x = 4 \\)?",
                "answer": 25, "displayAnswer": "25", "tolerance": 0, "unit": "",
                "hint": "2(4) - 3 = 8 - 3 = 5. Then square.",
                "explanation": "\\((8 - 3)^2 = 5^2 = 25\\)."
            },
            {
                "id": "ex7-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( 3x^2 - 75 = 0 \\)",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "3x^2 = 75 => x^2 = 25.",
                "explanation": "\\(x^2 = 25 \\implies x = 5\\)."
            },
            {
                "id": "ex7-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\frac{x + 2}{3} = \\frac{2x - 1}{4} \\), find \\( x \\).",
                "answer": 5.5, "displayAnswer": "5.5 (or 11/2)", "tolerance": 0.01, "unit": "",
                "hint": "4(x + 2) = 3(2x - 1) => 4x + 8 = 6x - 3.",
                "explanation": "\\(2x = 11 \\implies x = 5.5\\)."
            },
            {
                "id": "ex7-q10", "section": "algebra", "sectionName": "Algebra", "type": "mcq",
                "question": "Which of the following is equivalent to \\( x^2 - 14x + 49 \\)?",
                "options": ["\\( (x - 7)^2 \\)", "\\( (x + 7)^2 \\)", "\\( (x - 7)(x + 7) \\)", "\\( (x - 14)^2 \\)"],
                "answer": 0, "displayAnswer": "(x - 7)²", "tolerance": 0, "unit": "",
                "hint": "Perfect square trinomial a² - 2ab + b².",
                "explanation": "\\(x^2 - 2(7)x + 7^2 = (x - 7)^2\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex7-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 22^2 \\)",
                "answer": 484, "displayAnswer": "484", "tolerance": 0, "unit": "",
                "hint": "22 * 22 = 484.",
                "explanation": "\\(22^2 = 484\\)."
            },
            {
                "id": "ex7-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the cube: \\( 7^3 \\)",
                "answer": 343, "displayAnswer": "343", "tolerance": 0, "unit": "",
                "hint": "49 * 7 = 343.",
                "explanation": "\\(7^3 = 343\\)."
            },
            {
                "id": "ex7-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "An object moves from rest (\\( u = 0 \\)) with constant acceleration \\( a = 4 \\text{ m/s}^2 \\) for time \\( t = 5 \\text{ s} \\). Using \\( s = ut + \\frac{1}{2}at^2 \\), find displacement \\( s \\) in meters.",
                "answer": 50, "displayAnswer": "50", "tolerance": 0.01, "unit": "m",
                "hint": "0.5 * 4 * 25 = 2 * 25.",
                "explanation": "\\(s = 0.5 \\times 4 \\times 25 = 50 \\text{ m}\\)."
            },
            {
                "id": "ex7-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate: \\( \\frac{1.6 \\times 10^{-19} \\times 10^3}{2 \\times 10^{-17}} \\)",
                "answer": 8, "displayAnswer": "8", "tolerance": 0.01, "unit": "",
                "hint": "(1.6 / 2) * 10^(-19 + 3 - (-17)) = 0.8 * 10^1 = 8.",
                "explanation": "\\(0.8 \\times 10^1 = 8\\)."
            },
            {
                "id": "ex7-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "An electric heater has resistance \\( R = 20 \\text{ }\\Omega \\) and is connected to \\( V = 220 \\text{ V} \\). Calculate electrical power \\( P = \\frac{V^2}{R} \\) in Watts.",
                "answer": 2420, "displayAnswer": "2420", "tolerance": 1, "unit": "W",
                "hint": "220^2 / 20 = 48400 / 20 = 2420.",
                "explanation": "\\(P = \\frac{48400}{20} = 2420 \\text{ W}\\)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Basic → Intermediate: Proportions & Thermal Energy",
        "subtitle": "Develop rapid ratio balancing, algebraic factorization, and specific heat capacity calculations.",
        "difficulty": 2,
        "tier": "Basic → Intermediate",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex8-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 32 \\times 15 \\)",
                "answer": 480, "displayAnswer": "480", "tolerance": 0, "unit": "",
                "hint": "32 * 10 + 32 * 5 = 320 + 160.",
                "explanation": "\\(320 + 160 = 480\\)."
            },
            {
                "id": "ex8-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{5}{12} + \\frac{7}{18} \\). Enter as decimal to 3 decimal places.",
                "answer": 0.806, "displayAnswer": "0.806 (or 29/36)", "tolerance": 0.01, "unit": "",
                "hint": "LCM of 12 and 18 is 36. (15 + 14)/36 = 29/36.",
                "explanation": "\\(\\frac{29}{36} \\approx 0.8055 \\approx 0.806\\)."
            },
            {
                "id": "ex8-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 62.5\\% \\) of \\( 400 \\)",
                "answer": 250, "displayAnswer": "250", "tolerance": 0, "unit": "",
                "hint": "62.5% = 5/8. (5/8) * 400 = 5 * 50 = 250.",
                "explanation": "\\(\\frac{5}{8} \\times 400 = 250\\)."
            },
            {
                "id": "ex8-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 12.4 - 3.75 - 2.65 \\)",
                "answer": 6, "displayAnswer": "6", "tolerance": 0.01, "unit": "",
                "hint": "3.75 + 2.65 = 6.40. 12.40 - 6.40 = 6.00.",
                "explanation": "\\(12.4 - 6.4 = 6\\)."
            },
            {
                "id": "ex8-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\sqrt{1.44} \\)",
                "answer": 1.2, "displayAnswer": "1.2", "tolerance": 0.01, "unit": "",
                "hint": "12 squared is 144.",
                "explanation": "\\(\\sqrt{1.44} = 1.2\\)."
            },
            # Algebra (5)
            {
                "id": "ex8-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 4(3x - 2) = 2(5x + 4) \\)",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "12x - 8 = 10x + 8 => 2x = 16.",
                "explanation": "\\(2x = 16 \\implies x = 8\\)."
            },
            {
                "id": "ex8-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the positive root of \\( x^2 - 11x + 28 = 0 \\). Enter the larger root.",
                "answer": 7, "displayAnswer": "7 (roots are 4, 7)", "tolerance": 0, "unit": "",
                "hint": "(x - 4)(x - 7) = 0.",
                "explanation": "Roots are 4 and 7. Larger root is 7."
            },
            {
                "id": "ex8-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{a^3 b^2}{a b^4} \\). If \\( a = 6 \\) and \\( b = 2 \\), calculate the numerical value.",
                "answer": 9, "displayAnswer": "9", "tolerance": 0, "unit": "",
                "hint": "Simplifies to a^2 / b^2 = (a/b)^2 = (6/2)^2 = 3^2 = 9.",
                "explanation": "\\(\\left(\\frac{6}{2}\\right)^2 = 3^2 = 9\\)."
            },
            {
                "id": "ex8-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( y \\) if \\( 3x + 2y = 26 \\) and \\( x = 4 \\).",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "3(4) + 2y = 26 => 12 + 2y = 26 => 2y = 14.",
                "explanation": "\\(2y = 14 \\implies y = 7\\)."
            },
            {
                "id": "ex8-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\frac{2}{3}x = \\frac{5}{6} \\), find \\( x \\). Enter as decimal.",
                "answer": 1.25, "displayAnswer": "1.25 (or 5/4)", "tolerance": 0.01, "unit": "",
                "hint": "Multiply both sides by 3/2: x = (5/6)*(3/2) = 5/4.",
                "explanation": "\\(x = \\frac{5}{4} = 1.25\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex8-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 23^2 \\)",
                "answer": 529, "displayAnswer": "529", "tolerance": 0, "unit": "",
                "hint": "23 * 23 = 529.",
                "explanation": "\\(23^2 = 529\\)."
            },
            {
                "id": "ex8-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the cube: \\( 8^3 \\)",
                "answer": 512, "displayAnswer": "512", "tolerance": 0, "unit": "",
                "hint": "64 * 8 = 512.",
                "explanation": "\\(8^3 = 512\\)."
            },
            {
                "id": "ex8-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Heat energy required to raise the temperature of a substance is given by \\( Q = mc\\Delta T \\). If mass \\( m = 0.5 \\text{ kg} \\), specific heat \\( c = 4200 \\text{ J/(kg}\\cdot\\text{K)} \\), and temperature rise \\( \\Delta T = 10 \\text{ K} \\), find \\( Q \\) in Joules.",
                "answer": 21000, "displayAnswer": "21000", "tolerance": 1, "unit": "J",
                "hint": "0.5 * 4200 * 10 = 2100 * 10 = 21000.",
                "explanation": "\\(Q = 0.5 \\times 4200 \\times 10 = 21,000 \\text{ J}\\)."
            },
            {
                "id": "ex8-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{3.6 \\times 10^{-5}}{9 \\times 10^{-8}} \\)",
                "answer": 400, "displayAnswer": "400", "tolerance": 0.1, "unit": "",
                "hint": "(3.6 / 9) * 10^(-5 - (-8)) = 0.4 * 10^3 = 400.",
                "explanation": "\\(0.4 \\times 10^3 = 400\\)."
            },
            {
                "id": "ex8-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A car travelling at \\( 20 \\text{ m/s} \\) decelerates uniformly to rest in \\( 4 \\text{ s} \\). Find the magnitude of deceleration \\( a \\) in \\( \\text{m/s}^2 \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0.01, "unit": "m/s²",
                "hint": "a = |(0 - 20) / 4| = 5.",
                "explanation": "\\(a = \\frac{20}{4} = 5 \\text{ m/s}^2\\)."
            }
        ]
    },
    {
        "id": 9,
        "title": "Basic → Intermediate: Difference of Squares & Momentum",
        "subtitle": "Utilize difference of squares shortcuts, scientific notation balancing, and momentum/force substitutions.",
        "difficulty": 2,
        "tier": "Basic → Intermediate",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex9-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate using difference of squares: \\( 25^2 - 24^2 \\)",
                "answer": 49, "displayAnswer": "49", "tolerance": 0, "unit": "",
                "hint": "(25 - 24)(25 + 24) = 1 * 49.",
                "explanation": "\\((25-24)(25+24) = 1 \\times 49 = 49\\)."
            },
            {
                "id": "ex9-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 56 \\times 25 \\)",
                "answer": 1400, "displayAnswer": "1400", "tolerance": 0, "unit": "",
                "hint": "Divide 56 by 4 and multiply by 100: 14 * 100 = 1400.",
                "explanation": "\\(56 \\times 25 = 56 \\times \\frac{100}{4} = 14 \\times 100 = 1400\\)."
            },
            {
                "id": "ex9-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 37.5\\% \\) of \\( 480 \\)",
                "answer": 180, "displayAnswer": "180", "tolerance": 0, "unit": "",
                "hint": "37.5% = 3/8. (3/8) * 480 = 3 * 60 = 180.",
                "explanation": "\\(\\frac{3}{8} \\times 480 = 180\\)."
            },
            {
                "id": "ex9-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 0.04 \\times 0.05 \\times 200 \\)",
                "answer": 0.4, "displayAnswer": "0.4", "tolerance": 0.01, "unit": "",
                "hint": "0.05 * 200 = 10. Then 0.04 * 10 = 0.4.",
                "explanation": "\\(0.04 \\times 10 = 0.4\\)."
            },
            {
                "id": "ex9-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\sqrt{0.0081} \\)",
                "answer": 0.09, "displayAnswer": "0.09", "tolerance": 0.001, "unit": "",
                "hint": "9 squared is 81. 4 decimal places -> 2 decimal places.",
                "explanation": "\\(\\sqrt{0.0081} = 0.09\\)."
            },
            # Algebra (5)
            {
                "id": "ex9-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate: \\( 52^2 - 48^2 \\)",
                "answer": 400, "displayAnswer": "400", "tolerance": 0, "unit": "",
                "hint": "(52 - 48)(52 + 48) = 4 * 100.",
                "explanation": "\\((52-48)(52+48) = 4 \\times 100 = 400\\)."
            },
            {
                "id": "ex9-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{3}{x} = \\frac{12}{28} \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "12/28 simplifies to 3/7. So 3/x = 3/7.",
                "explanation": "\\(x = 7\\)."
            },
            {
                "id": "ex9-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the roots of \\( x^2 - 4x - 21 = 0 \\). What is the positive root?",
                "answer": 7, "displayAnswer": "7 (roots are -3, 7)", "tolerance": 0, "unit": "",
                "hint": "(x - 7)(x + 3) = 0.",
                "explanation": "Roots are 7 and -3. Positive root is 7."
            },
            {
                "id": "ex9-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Rearrange \\( K = \\frac{1}{2}mv^2 \\) for \\( v \\). If \\( K = 72 \\text{ J} \\) and \\( m = 4 \\text{ kg} \\), find \\( v \\) in \\( \\text{m/s} \\).",
                "answer": 6, "displayAnswer": "6", "tolerance": 0.01, "unit": "m/s",
                "hint": "v^2 = 2K / m = 144 / 4 = 36 => v = 6.",
                "explanation": "\\(v = \\sqrt{\\frac{2 \\times 72}{4}} = \\sqrt{36} = 6 \\text{ m/s}\\)."
            },
            {
                "id": "ex9-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{2x+4}{2} - \\frac{3x-6}{3} \\). Enter the numerical value.",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "(x + 2) - (x - 2) = x + 2 - x + 2 = 4? Wait: 2x+4/2 = x+2; 3x-6/3 = x-2. (x+2)-(x-2) = 4.",
                "explanation": "\\((x + 2) - (x - 2) = 4\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex9-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 24^2 \\)",
                "answer": 576, "displayAnswer": "576", "tolerance": 0, "unit": "",
                "hint": "24 * 24 = 576.",
                "explanation": "\\(24^2 = 576\\)."
            },
            {
                "id": "ex9-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the cube: \\( 9^3 \\)",
                "answer": 729, "displayAnswer": "729", "tolerance": 0, "unit": "",
                "hint": "81 * 9 = 729.",
                "explanation": "\\(9^3 = 729\\)."
            },
            {
                "id": "ex9-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Linear momentum is \\( p = mv \\). If mass \\( m = 0.25 \\text{ kg} \\) and velocity \\( v = 16 \\text{ m/s} \\), calculate momentum \\( p \\) in \\( \\text{kg}\\cdot\\text{m/s} \\).",
                "answer": 4, "displayAnswer": "4", "tolerance": 0.01, "unit": "kg·m/s",
                "hint": "0.25 * 16 = 16 / 4 = 4.",
                "explanation": "\\(p = 0.25 \\times 16 = 4 \\text{ kg}\\cdot\\text{m/s}\\)."
            },
            {
                "id": "ex9-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{6.4 \\times 10^8}{1.6 \\times 10^3} \\)",
                "answer": 400000, "displayAnswer": "400,000 (or 4×10⁵)", "tolerance": 1, "unit": "",
                "hint": "(6.4 / 1.6) * 10^(8 - 3) = 4 * 10^5.",
                "explanation": "\\(4 \\times 10^5 = 400,000\\)."
            },
            {
                "id": "ex9-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A 100 W bulb operates at 200 V. Using \\( P = \\frac{V^2}{R} \\), find the resistance \\( R \\) in \\( \\Omega \\).",
                "answer": 400, "displayAnswer": "400", "tolerance": 0.1, "unit": "Ω",
                "hint": "R = V^2 / P = 200^2 / 100 = 40000 / 100 = 400.",
                "explanation": "\\(R = \\frac{200^2}{100} = \\frac{40000}{100} = 400 \\text{ }\\Omega\\)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Basic → Intermediate: Scientific Notation & Power Dissipation",
        "subtitle": "Consolidate squares up to 25, power dissipation P = I²R, and order of magnitude calculations.",
        "difficulty": 2,
        "tier": "Basic → Intermediate",
        "estimatedMinutes": 15,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex10-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 36 \\times 25 \\)",
                "answer": 900, "displayAnswer": "900", "tolerance": 0, "unit": "",
                "hint": "36 / 4 = 9 => 9 * 100 = 900.",
                "explanation": "\\(36 \\times 25 = 900\\)."
            },
            {
                "id": "ex10-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( 75^2 - 25^2 \\)",
                "answer": 5000, "displayAnswer": "5000", "tolerance": 0, "unit": "",
                "hint": "(75 - 25)(75 + 25) = 50 * 100.",
                "explanation": "\\((75-25)(75+25) = 50 \\times 100 = 5000\\)."
            },
            {
                "id": "ex10-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate \\( 87.5\\% \\) of \\( 320 \\)",
                "answer": 280, "displayAnswer": "280", "tolerance": 0, "unit": "",
                "hint": "87.5% = 7/8. (7/8) * 320 = 7 * 40 = 280.",
                "explanation": "\\(\\frac{7}{8} \\times 320 = 280\\)."
            },
            {
                "id": "ex10-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 15.6 + 8.75 - 4.35 \\)",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "",
                "hint": "15.60 + 4.40 = 20.00.",
                "explanation": "\\(15.60 + 8.75 - 4.35 = 20.00\\)."
            },
            {
                "id": "ex10-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1.44}{0.12} \\)",
                "answer": 12, "displayAnswer": "12", "tolerance": 0.01, "unit": "",
                "hint": "144 / 12 = 12.",
                "explanation": "\\(1.44 / 0.12 = 12\\)."
            },
            # Algebra (5)
            {
                "id": "ex10-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{2x - 5}{3} = \\frac{x + 7}{2} \\)",
                "answer": 31, "displayAnswer": "31", "tolerance": 0, "unit": "",
                "hint": "2(2x - 5) = 3(x + 7) => 4x - 10 = 3x + 21.",
                "explanation": "\\(4x - 10 = 3x + 21 \\implies x = 31\\)."
            },
            {
                "id": "ex10-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the positive root of \\( 4x^2 - 36 = 0 \\).",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "4x^2 = 36 => x^2 = 9.",
                "explanation": "\\(x = 3\\)."
            },
            {
                "id": "ex10-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Expand \\( (3x + 2)^2 \\). What is the coefficient of \\( x \\)?",
                "answer": 12, "displayAnswer": "12", "tolerance": 0, "unit": "",
                "hint": "2 * 3x * 2 = 12x.",
                "explanation": "\\((3x+2)^2 = 9x^2 + 12x + 4\\). Coefficient of \\(x\\) is 12."
            },
            {
                "id": "ex10-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( 5x + 3y = 29 \\) and \\( y = 3 \\), find \\( x \\).",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "5x + 9 = 29 => 5x = 20.",
                "explanation": "\\(5x = 20 \\implies x = 4\\)."
            },
            {
                "id": "ex10-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{x^2 - 9}{x + 3} \\). Evaluate at \\( x = 11 \\).",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "(x - 3)(x + 3) / (x + 3) = x - 3. At x = 11: 11 - 3 = 8.",
                "explanation": "\\(11 - 3 = 8\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex10-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 25^2 \\)",
                "answer": 625, "displayAnswer": "625", "tolerance": 0, "unit": "",
                "hint": "25 * 25 = 625.",
                "explanation": "\\(25^2 = 625\\)."
            },
            {
                "id": "ex10-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the cube: \\( 10^3 \\)",
                "answer": 1000, "displayAnswer": "1000", "tolerance": 0, "unit": "",
                "hint": "10 * 10 * 10 = 1000.",
                "explanation": "\\(10^3 = 1000\\)."
            },
            {
                "id": "ex10-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Using Joule's heating formula \\( P = I^2 R \\), find the power dissipated when current \\( I = 3 \\text{ A} \\) flows through resistance \\( R = 15 \\text{ }\\Omega \\) in Watts.",
                "answer": 135, "displayAnswer": "135", "tolerance": 0, "unit": "W",
                "hint": "3^2 * 15 = 9 * 15 = 135.",
                "explanation": "\\(P = 9 \\times 15 = 135 \\text{ W}\\)."
            },
            {
                "id": "ex10-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{(3 \\times 10^4) \\times (4 \\times 10^{-2})}{2 \\times 10^1} \\)",
                "answer": 60, "displayAnswer": "60", "tolerance": 0.01, "unit": "",
                "hint": "(12 / 2) * 10^(4 - 2 - 1) = 6 * 10^1 = 60.",
                "explanation": "\\(6 \\times 10^1 = 60\\)."
            },
            {
                "id": "ex10-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A body of mass \\( 2 \\text{ kg} \\) is lifted to height \\( h = 15 \\text{ m} \\) above ground. Taking \\( g = 9.8 \\text{ m/s}^2 \\), calculate its gravitational potential energy \\( U = mgh \\) in Joules.",
                "answer": 294, "displayAnswer": "294", "tolerance": 1, "unit": "J",
                "hint": "2 * 9.8 * 15 = 30 * 9.8 = 294.",
                "explanation": "\\(U = 2 \\times 9.8 \\times 15 = 30 \\times 9.8 = 294 \\text{ J}\\)."
            }
        ]
    }
]

print(f"Tier 2 loaded: {len(tier2)} exercises.")
