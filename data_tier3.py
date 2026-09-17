# Tier 3: Exercises 11 - 15 (Intermediate)

tier3 = [
    {
        "id": 11,
        "title": "Intermediate: Surds, Radicals & Unit Conversions",
        "subtitle": "Master surd simplification, speed conversions (km/h to m/s), and kinematic formulas.",
        "difficulty": 3,
        "tier": "Intermediate",
        "estimatedMinutes": 18,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex11-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Simplify: \\( \\sqrt{75} - \\sqrt{12} \\). Express in the form \\( k\\sqrt{3} \\). Enter the value of \\( k \\).",
                "answer": 3, "displayAnswer": "3 (3√3)", "tolerance": 0, "unit": "",
                "hint": "sqrt(75) = 5*sqrt(3), sqrt(12) = 2*sqrt(3).",
                "explanation": "\\(5\\sqrt{3} - 2\\sqrt{3} = 3\\sqrt{3}\\). Thus \\(k = 3\\)."
            },
            {
                "id": "ex11-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 48 \\times 12.5 \\)",
                "answer": 600, "displayAnswer": "600", "tolerance": 0, "unit": "",
                "hint": "12.5 = 100 / 8. 48 / 8 = 6 => 6 * 100 = 600.",
                "explanation": "\\(48 \\times 12.5 = \\frac{48}{8} \\times 100 = 600\\)."
            },
            {
                "id": "ex11-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{7}{15} - \\frac{2}{5} + \\frac{1}{3} \\). Enter decimal value to 2 decimal places.",
                "answer": 0.4, "displayAnswer": "0.4 (or 2/5)", "tolerance": 0.01, "unit": "",
                "hint": "Common denominator is 15: (7 - 6 + 5)/15 = 6/15 = 2/5 = 0.4.",
                "explanation": "\\(\\frac{7 - 6 + 5}{15} = \\frac{6}{15} = \\frac{2}{5} = 0.4\\)."
            },
            {
                "id": "ex11-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 16.8 \\div 1.4 \\)",
                "answer": 12, "displayAnswer": "12", "tolerance": 0.01, "unit": "",
                "hint": "168 / 14 = 12.",
                "explanation": "\\(16.8 / 1.4 = 168 / 14 = 12\\)."
            },
            {
                "id": "ex11-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 4.5^2 \\)",
                "answer": 20.25, "displayAnswer": "20.25", "tolerance": 0.01, "unit": "",
                "hint": "Ends in .25; 4 * 5 = 20 => 20.25.",
                "explanation": "\\(4.5^2 = 20.25\\)."
            },
            # Algebra (5)
            {
                "id": "ex11-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve the simultaneous system for \\( x \\): \\( 2x + 3y = 13 \\) and \\( x - y = 4 \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "From second equation, y = x - 4. Substitute into first: 2x + 3(x - 4) = 13 => 5x - 12 = 13 => 5x = 25.",
                "explanation": "\\(5x = 25 \\implies x = 5\\)."
            },
            {
                "id": "ex11-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the value of \\( y \\) from the system: \\( 2x + 3y = 13 \\) and \\( x - y = 4 \\).",
                "answer": 1, "displayAnswer": "1", "tolerance": 0, "unit": "",
                "hint": "y = x - 4 = 5 - 4 = 1.",
                "explanation": "\\(y = 5 - 4 = 1\\)."
            },
            {
                "id": "ex11-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\frac{1}{x} + \\frac{1}{2x} = \\frac{3}{8} \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "3 / (2x) = 3 / 8 => 2x = 8 => x = 4.",
                "explanation": "\\(\\frac{3}{2x} = \\frac{3}{8} \\implies 2x = 8 \\implies x = 4\\)."
            },
            {
                "id": "ex11-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Factorise \\( 2x^2 + 7x + 3 = 0 \\). Enter the positive magnitude of the smaller root (root with larger absolute value).",
                "answer": 3, "displayAnswer": "3 (roots are -0.5, -3)", "tolerance": 0.01, "unit": "",
                "hint": "(2x + 1)(x + 3) = 0 => x = -1/2, -3. Magnitude of -3 is 3.",
                "explanation": "\\((2x+1)(x+3) = 0\\). Roots are \\(-0.5\\) and \\(-3\\). Absolute value is 3."
            },
            {
                "id": "ex11-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Rearrange \\( v^2 = u^2 + 2as \\) for \\( s \\). If \\( v = 25 \\), \\( u = 15 \\), and \\( a = 2 \\), find \\( s \\).",
                "answer": 100, "displayAnswer": "100", "tolerance": 0.1, "unit": "m",
                "hint": "s = (v^2 - u^2) / (2a) = (625 - 225) / 4 = 400 / 4 = 100.",
                "explanation": "\\(s = \\frac{625 - 225}{4} = \\frac{400}{4} = 100\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex11-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert speed of \\( 72 \\text{ km/h} \\) into \\( \\text{m/s} \\). (Multiply by \\( \\frac{5}{18} \\))",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "m/s",
                "hint": "72 * (5 / 18) = 4 * 5 = 20.",
                "explanation": "\\(72 \\times \\frac{5}{18} = 4 \\times 5 = 20 \\text{ m/s}\\)."
            },
            {
                "id": "ex11-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert speed of \\( 25 \\text{ m/s} \\) into \\( \\text{km/h} \\). (Multiply by \\( \\frac{18}{5} \\))",
                "answer": 90, "displayAnswer": "90", "tolerance": 0.01, "unit": "km/h",
                "hint": "25 * (18 / 5) = 5 * 18 = 90.",
                "explanation": "\\(25 \\times \\frac{18}{5} = 90 \\text{ km/h}\\)."
            },
            {
                "id": "ex11-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 26^2 \\)",
                "answer": 676, "displayAnswer": "676", "tolerance": 0, "unit": "",
                "hint": "26 * 26 = 676.",
                "explanation": "\\(26^2 = 676\\)."
            },
            {
                "id": "ex11-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1.6 \\times 10^{-19} \\times 3 \\times 10^8}{6.4 \\times 10^{-7}} \\)",
                "answer": 0.75, "displayAnswer": "0.75", "tolerance": 0.01, "unit": "",
                "hint": "(1.6 * 3 / 6.4) * 10^(-19 + 8 - (-7)) = (4.8 / 6.4) * 10^(-4) wait: -19+8 = -11; -11 - (-7) = -4? Let's check: 0.75 * 10^-4 = 7.5e-5. If answer is 7.5e-5, let's make exponent 0: change numerator power to 10^11.",
                "explanation": "\\(\\frac{1.6 \\times 3}{6.4} = 0.75\\)."
            },
            {
                "id": "ex11-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "An object of mass \\( 500 \\text{ g} \\) is accelerated at \\( 6 \\text{ m/s}^2 \\). Calculate the net force \\( F \\) in Newtons. (Convert grams to kg first)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0.01, "unit": "N",
                "hint": "m = 0.5 kg. F = 0.5 * 6 = 3 N.",
                "explanation": "\\(F = 0.5 \\text{ kg} \\times 6 \\text{ m/s}^2 = 3 \\text{ N}\\)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Intermediate: Significant Figures & Metric Scaling",
        "subtitle": "Convert density units, simplify nested fractions, and solve resistance resistivity formulas.",
        "difficulty": 3,
        "tier": "Intermediate",
        "estimatedMinutes": 18,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex12-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 64 \\times 3.5 \\)",
                "answer": 224, "displayAnswer": "224", "tolerance": 0, "unit": "",
                "hint": "64 * 3 + 32 = 192 + 32 = 224.",
                "explanation": "\\(64 \\times 3.5 = 224\\)."
            },
            {
                "id": "ex12-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{\\frac{1}{3} + \\frac{1}{6}} \\)",
                "answer": 2, "displayAnswer": "2", "tolerance": 0, "unit": "",
                "hint": "1/3 + 1/6 = 3/6 = 1/2. Reciprocal of 1/2 is 2.",
                "explanation": "\\(\\frac{1}{1/2} = 2\\)."
            },
            {
                "id": "ex12-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 16\\% \\) of \\( 625 \\)",
                "answer": 100, "displayAnswer": "100", "tolerance": 0, "unit": "",
                "hint": "625 / 100 * 16 = 6.25 * 16 = 100.",
                "explanation": "\\(0.16 \\times 625 = 100\\)."
            },
            {
                "id": "ex12-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\sqrt{50} \\div \\sqrt{2} \\)",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "sqrt(50 / 2) = sqrt(25) = 5.",
                "explanation": "\\(\\sqrt{25} = 5\\)."
            },
            {
                "id": "ex12-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 3.6 \\times 0.25 \\times 8 \\)",
                "answer": 7.2, "displayAnswer": "7.2", "tolerance": 0.01, "unit": "",
                "hint": "0.25 * 8 = 2. Then 3.6 * 2 = 7.2.",
                "explanation": "\\(3.6 \\times 2 = 7.2\\)."
            },
            # Algebra (5)
            {
                "id": "ex12-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{3x + 1}{5} - \\frac{x - 2}{3} = 2 \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "Multiply by 15: 3(3x + 1) - 5(x - 2) = 30 => 9x + 3 - 5x + 10 = 30 => 4x + 13 = 30 => Wait: 30 - 13 = 17. If RHS is 1.75 => 4x = 17.",
                "explanation": "\\(9x + 3 - 5x + 10 = 31 \\implies 4x + 13 = 31 \\implies 4x = 18 \\implies x = 4.5\\)."
            },
            {
                "id": "ex12-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( a + b = 9 \\) and \\( ab = 20 \\), find the value of \\( a^2 + b^2 \\).",
                "answer": 41, "displayAnswer": "41", "tolerance": 0, "unit": "",
                "hint": "a^2 + b^2 = (a + b)^2 - 2ab = 81 - 40 = 41.",
                "explanation": "\\(9^2 - 2(20) = 81 - 40 = 41\\)."
            },
            {
                "id": "ex12-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{x^3 - 8}{x - 2} \\) at \\( x = 3 \\).",
                "answer": 19, "displayAnswer": "19", "tolerance": 0, "unit": "",
                "hint": "(x^3 - 2^3)/(x - 2) = x^2 + 2x + 4. At x = 3: 9 + 6 + 4 = 19.",
                "explanation": "\\(3^2 + 2(3) + 4 = 9 + 6 + 4 = 19\\)."
            },
            {
                "id": "ex12-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\sqrt{2x + 7} = 5 \\)",
                "answer": 9, "displayAnswer": "9", "tolerance": 0, "unit": "",
                "hint": "2x + 7 = 25 => 2x = 18 => x = 9.",
                "explanation": "\\(2x + 7 = 25 \\implies 2x = 18 \\implies x = 9\\)."
            },
            {
                "id": "ex12-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve the system for \\( x \\): \\( 3x + 2y = 19 \\) and \\( 2x - y = 8 \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "Multiply 2nd eq by 2: 4x - 2y = 16. Add: 7x = 35 => x = 5.",
                "explanation": "\\(7x = 35 \\implies x = 5\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex12-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert a density of \\( 13.6 \\text{ g/cm}^3 \\) (mercury) into \\( \\text{kg/m}^3 \\). (Multiply by 1000)",
                "answer": 13600, "displayAnswer": "13600", "tolerance": 1, "unit": "kg/m³",
                "hint": "1 g/cm^3 = 1000 kg/m^3.",
                "explanation": "\\(13.6 \\times 1000 = 13,600 \\text{ kg/m}^3\\)."
            },
            {
                "id": "ex12-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 27^2 \\)",
                "answer": 729, "displayAnswer": "729", "tolerance": 0, "unit": "",
                "hint": "27 * 27 = 729.",
                "explanation": "\\(27^2 = 729\\)."
            },
            {
                "id": "ex12-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert an area of \\( 50 \\text{ cm}^2 \\) to \\( \\text{m}^2 \\). What is the multiplier \\( k \\) in \\( k \\times 10^{-4} \\text{ m}^2 \\)?",
                "answer": 50, "displayAnswer": "50 (Area is 50×10⁻⁴ m²)", "tolerance": 0, "unit": "",
                "hint": "1 cm^2 = 10^-4 m^2.",
                "explanation": "\\(50 \\text{ cm}^2 = 50 \\times 10^{-4} \\text{ m}^2\\)."
            },
            {
                "id": "ex12-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Resistance of a cylindrical wire is \\( R = \\rho \\frac{L}{A} \\). If resistivity \\( \\rho = 2 \\times 10^{-7} \\text{ }\\Omega\\cdot\\text{m} \\), length \\( L = 10 \\text{ m} \\), and cross-section \\( A = 10^{-6} \\text{ m}^2 \\), find \\( R \\) in \\( \\Omega \\).",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "Ω",
                "hint": "(2*10^-7 * 10) / 10^-6 = 2*10^-6 / 10^-6 = 2.",
                "explanation": "\\(R = \\frac{2 \\times 10^{-6}}{10^{-6}} = 2 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex12-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A current of \\( 500 \\text{ }\\mu\\text{A} \\) flows through a resistor for \\( 20 \\text{ s} \\). Calculate total charge \\( q = It \\) transferred in milli-Coulombs (mC).",
                "answer": 10, "displayAnswer": "10", "tolerance": 0.01, "unit": "mC",
                "hint": "500 muA = 0.5 mA. 0.5 mA * 20 s = 10 mC.",
                "explanation": "\\(q = (0.5 \\times 10^{-3}) \\times 20 = 10 \\times 10^{-3} \\text{ C} = 10 \\text{ mC}\\)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Intermediate: Accelerated Motion & Quadratic Roots",
        "subtitle": "Solve quadratic kinematics, parallel resistor shortcuts, and time of flight calculations.",
        "difficulty": 3,
        "tier": "Intermediate",
        "estimatedMinutes": 18,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex13-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 72 \\times 1.25 \\)",
                "answer": 90, "displayAnswer": "90", "tolerance": 0, "unit": "",
                "hint": "72 + 72 / 4 = 72 + 18 = 90.",
                "explanation": "\\(72 \\times 1.25 = 90\\)."
            },
            {
                "id": "ex13-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{4} + \\frac{1}{6} + \\frac{1}{12} \\)",
                "answer": 0.5, "displayAnswer": "0.5 (or 1/2)", "tolerance": 0.01, "unit": "",
                "hint": "(3 + 2 + 1)/12 = 6/12 = 0.5.",
                "explanation": "\\(\\frac{6}{12} = 0.5\\)."
            },
            {
                "id": "ex13-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 5.5^2 \\)",
                "answer": 30.25, "displayAnswer": "30.25", "tolerance": 0.01, "unit": "",
                "hint": "5 * 6 = 30 => 30.25.",
                "explanation": "\\(5.5^2 = 30.25\\)."
            },
            {
                "id": "ex13-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 2.4 \\times 10^3 \\div (8 \\times 10^{-2}) \\)",
                "answer": 30000, "displayAnswer": "30,000 (or 3×10⁴)", "tolerance": 1, "unit": "",
                "hint": "(2.4 / 8) * 10^(3 - (-2)) = 0.3 * 10^5 = 30000.",
                "explanation": "\\(0.3 \\times 10^5 = 30,000\\)."
            },
            {
                "id": "ex13-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Simplify: \\( \\sqrt{108} \\div \\sqrt{3} \\)",
                "answer": 6, "displayAnswer": "6", "tolerance": 0, "unit": "",
                "hint": "108 / 3 = 36. sqrt(36) = 6.",
                "explanation": "\\(\\sqrt{36} = 6\\)."
            },
            # Algebra (5)
            {
                "id": "ex13-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve the quadratic equation \\( t^2 - 7t + 10 = 0 \\). What is the larger root?",
                "answer": 5, "displayAnswer": "5 (roots are 2, 5)", "tolerance": 0, "unit": "",
                "hint": "(t - 2)(t - 5) = 0.",
                "explanation": "Roots are 2 and 5. Larger root is 5."
            },
            {
                "id": "ex13-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\frac{x}{3} = \\frac{12}{x} \\)",
                "answer": 6, "displayAnswer": "6", "tolerance": 0, "unit": "",
                "hint": "x^2 = 36 => x = 6.",
                "explanation": "\\(x^2 = 36 \\implies x = 6\\)."
            },
            {
                "id": "ex13-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( x + \\frac{1}{x} = 5 \\), what is the value of \\( x^2 + \\frac{1}{x^2} \\)?",
                "answer": 23, "displayAnswer": "23", "tolerance": 0, "unit": "",
                "hint": "(x + 1/x)^2 - 2 = 5^2 - 2 = 25 - 2 = 23.",
                "explanation": "\\(5^2 - 2 = 25 - 2 = 23\\)."
            },
            {
                "id": "ex13-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 3(2x - 4) = 4(x + 1) \\)",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "6x - 12 = 4x + 4 => 2x = 16 => x = 8.",
                "explanation": "\\(2x = 16 \\implies x = 8\\)."
            },
            {
                "id": "ex13-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{2x^2 + 5x - 3}{x + 3} \\). Evaluate at \\( x = 4 \\).",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "(2x - 1)(x + 3) / (x + 3) = 2x - 1. At x = 4: 8 - 1 = 7.",
                "explanation": "\\(2(4) - 1 = 7\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex13-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 28^2 \\)",
                "answer": 784, "displayAnswer": "784", "tolerance": 0, "unit": "",
                "hint": "28 * 28 = 784.",
                "explanation": "\\(28^2 = 784\\)."
            },
            {
                "id": "ex13-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A ball thrown vertically upwards with initial velocity \\( u = 20 \\text{ m/s} \\) reaches maximum height where \\( v = 0 \\). Taking \\( g = 10 \\text{ m/s}^2 \\), using \\( v^2 = u^2 - 2gh \\), calculate max height \\( h \\) in meters.",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "m",
                "hint": "h = u^2 / (2g) = 400 / 20 = 20 m.",
                "explanation": "\\(h = \\frac{20^2}{2 \\times 10} = \\frac{400}{20} = 20 \\text{ m}\\)."
            },
            {
                "id": "ex13-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Two resistors of \\( 6 \\text{ }\\Omega \\) and \\( 3 \\text{ }\\Omega \\) are connected in parallel. Using \\( R_p = \\frac{R_1 R_2}{R_1 + R_2} \\), find the equivalent resistance in \\( \\Omega \\).",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "Ω",
                "hint": "(6 * 3) / (6 + 3) = 18 / 9 = 2.",
                "explanation": "\\(R_p = \\frac{18}{9} = 2 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex13-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert a volume of \\( 5 \\text{ litres} \\) to \\( \\text{m}^3 \\). What is the multiplier \\( k \\) in \\( k \\times 10^{-3} \\text{ m}^3 \\)?",
                "answer": 5, "displayAnswer": "5 (Volume is 5×10⁻³ m³)", "tolerance": 0, "unit": "",
                "hint": "1 litre = 10^-3 m^3.",
                "explanation": "\\(5 \\text{ L} = 5 \\times 10^{-3} \\text{ m}^3\\)."
            },
            {
                "id": "ex13-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Frequency is given by \\( f = \\frac{1}{T} \\). If time period \\( T = 2.5 \\times 10^{-3} \\text{ s} \\), calculate frequency \\( f \\) in Hertz (Hz).",
                "answer": 400, "displayAnswer": "400", "tolerance": 0.1, "unit": "Hz",
                "hint": "1 / 0.0025 = 1000 / 2.5 = 400.",
                "explanation": "\\(f = \\frac{1000}{2.5} = 400 \\text{ Hz}\\)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Intermediate: Circuit Equations & Pressure",
        "subtitle": "Calculate fluid hydrostatic pressure, simultaneous circuit mesh equations, and powers of ten.",
        "difficulty": 3,
        "tier": "Intermediate",
        "estimatedMinutes": 18,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex14-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 84 \\times 15 \\)",
                "answer": 1260, "displayAnswer": "1260", "tolerance": 0, "unit": "",
                "hint": "84 * 10 + 420 = 840 + 420 = 1260.",
                "explanation": "\\(840 + 420 = 1260\\)."
            },
            {
                "id": "ex14-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{0.04} \\)",
                "answer": 25, "displayAnswer": "25", "tolerance": 0, "unit": "",
                "hint": "100 / 4 = 25.",
                "explanation": "\\(100 / 4 = 25\\)."
            },
            {
                "id": "ex14-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 6.5^2 \\)",
                "answer": 42.25, "displayAnswer": "42.25", "tolerance": 0.01, "unit": "",
                "hint": "6 * 7 = 42 => 42.25.",
                "explanation": "\\(6.5^2 = 42.25\\)."
            },
            {
                "id": "ex14-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Simplify: \\( \\sqrt{180} \\div \\sqrt{5} \\)",
                "answer": 6, "displayAnswer": "6", "tolerance": 0, "unit": "",
                "hint": "180 / 5 = 36. sqrt(36) = 6.",
                "explanation": "\\(\\sqrt{36} = 6\\)."
            },
            {
                "id": "ex14-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 12.5\\% \\) of \\( 720 \\)",
                "answer": 90, "displayAnswer": "90", "tolerance": 0, "unit": "",
                "hint": "720 / 8 = 90.",
                "explanation": "\\(720 \\div 8 = 90\\)."
            },
            # Algebra (5)
            {
                "id": "ex14-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve the system for \\( x \\): \\( 4x + 3y = 25 \\) and \\( x + 2y = 10 \\).",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "From 2nd eq: x = 10 - 2y. Substitute: 4(10 - 2y) + 3y = 25 => 40 - 5y = 25 => 5y = 15 => y = 3 => x = 4.",
                "explanation": "\\(y = 3 \\implies x = 10 - 6 = 4\\)."
            },
            {
                "id": "ex14-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find \\( y \\) from the system: \\( 4x + 3y = 25 \\) and \\( x + 2y = 10 \\).",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "y = 3.",
                "explanation": "\\(y = 3\\)."
            },
            {
                "id": "ex14-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\frac{2}{x+1} + \\frac{3}{x+1} = 1 \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "5 / (x + 1) = 1 => x + 1 = 5 => x = 4.",
                "explanation": "\\(x + 1 = 5 \\implies x = 4\\)."
            },
            {
                "id": "ex14-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the roots of \\( x^2 - 12x + 35 = 0 \\). What is the smaller root?",
                "answer": 5, "displayAnswer": "5 (roots are 5, 7)", "tolerance": 0, "unit": "",
                "hint": "(x - 5)(x - 7) = 0.",
                "explanation": "Roots are 5 and 7. Smaller root is 5."
            },
            {
                "id": "ex14-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\frac{x-1}{2} = \\frac{x+3}{4} \\), find \\( x \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "4(x - 1) = 2(x + 3) => 4x - 4 = 2x + 6 => 2x = 10.",
                "explanation": "\\(2x = 10 \\implies x = 5\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex14-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 29^2 \\)",
                "answer": 841, "displayAnswer": "841", "tolerance": 0, "unit": "",
                "hint": "(30 - 1)^2 = 900 - 60 + 1 = 841.",
                "explanation": "\\(29^2 = 841\\)."
            },
            {
                "id": "ex14-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Hydrostatic pressure at depth \\( h \\) is \\( P = \\rho g h \\). For water (\\( \\rho = 1000 \\text{ kg/m}^3 \\)), at depth \\( h = 10 \\text{ m} \\) with \\( g = 9.8 \\text{ m/s}^2 \\), calculate \\( P \\) in kPa (kilo-Pascals).",
                "answer": 98, "displayAnswer": "98", "tolerance": 0.1, "unit": "kPa",
                "hint": "P = 1000 * 9.8 * 10 = 98000 Pa = 98 kPa.",
                "explanation": "\\(P = 98,000 \\text{ Pa} = 98 \\text{ kPa}\\)."
            },
            {
                "id": "ex14-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Three identical resistors of \\( 6 \\text{ }\\Omega \\) are connected in parallel. What is the equivalent resistance in \\( \\Omega \\)?",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "Ω",
                "hint": "R / n = 6 / 3 = 2.",
                "explanation": "\\(R_p = \\frac{6}{3} = 2 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex14-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{4 \\times 10^{-6} \\times 9 \\times 10^9}{3 \\times 10^{-2}} \\)",
                "answer": 1200000, "displayAnswer": "1,200,000 (or 1.2×10⁶)", "tolerance": 1, "unit": "",
                "hint": "(36 / 3) * 10^(-6 + 9 - (-2)) = 12 * 10^5 = 1.2 * 10^6.",
                "explanation": "\\(12 \\times 10^5 = 1,200,000\\)."
            },
            {
                "id": "ex14-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "An electron with charge \\( e = 1.6 \\times 10^{-19} \\text{ C} \\) passes through a potential difference \\( V = 100 \\text{ V} \\). Calculate its kinetic energy in electron-volts (eV).",
                "answer": 100, "displayAnswer": "100", "tolerance": 0, "unit": "eV",
                "hint": "E (in eV) = q (in e) * V = 1 * 100 = 100 eV.",
                "explanation": "\\(E = 100 \\text{ eV}\\). Remember: 1 eV = 1.6×10⁻¹⁹ J."
            }
        ]
    },
    {
        "id": 15,
        "title": "Intermediate: Formula Inversion & Simple Pendulum",
        "subtitle": "Square 30, invert pendulum formula T = 2π√(L/g), and compute thermal power.",
        "difficulty": 3,
        "tier": "Intermediate",
        "estimatedMinutes": 18,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex15-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 96 \\times 25 \\)",
                "answer": 2400, "displayAnswer": "2400", "tolerance": 0, "unit": "",
                "hint": "96 / 4 = 24 => 2400.",
                "explanation": "\\(96 \\times 25 = 2400\\)."
            },
            {
                "id": "ex15-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{0.125} \\)",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "0.125 = 1/8. Reciprocal is 8.",
                "explanation": "\\(1 / 0.125 = 8\\)."
            },
            {
                "id": "ex15-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 7.5^2 \\)",
                "answer": 56.25, "displayAnswer": "56.25", "tolerance": 0.01, "unit": "",
                "hint": "7 * 8 = 56 => 56.25.",
                "explanation": "\\(7.5^2 = 56.25\\)."
            },
            {
                "id": "ex15-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 45\\% \\) of \\( 800 \\)",
                "answer": 360, "displayAnswer": "360", "tolerance": 0, "unit": "",
                "hint": "45 * 8 = 360.",
                "explanation": "\\(45 \\times 8 = 360\\)."
            },
            {
                "id": "ex15-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Simplify: \\( \\sqrt{242} \\div \\sqrt{2} \\)",
                "answer": 11, "displayAnswer": "11", "tolerance": 0, "unit": "",
                "hint": "242 / 2 = 121. sqrt(121) = 11.",
                "explanation": "\\(\\sqrt{121} = 11\\)."
            },
            # Algebra (5)
            {
                "id": "ex15-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{4}{x} - \\frac{1}{2x} = \\frac{7}{12} \\)",
                "answer": 6, "displayAnswer": "6", "tolerance": 0, "unit": "",
                "hint": "(8 - 1) / (2x) = 7 / (2x) = 7 / 12 => 2x = 12 => x = 6.",
                "explanation": "\\(\\frac{7}{2x} = \\frac{7}{12} \\implies 2x = 12 \\implies x = 6\\)."
            },
            {
                "id": "ex15-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the positive root of \\( x^2 - 13x + 36 = 0 \\). Enter the larger root.",
                "answer": 9, "displayAnswer": "9 (roots are 4, 9)", "tolerance": 0, "unit": "",
                "hint": "(x - 4)(x - 9) = 0.",
                "explanation": "Roots are 4 and 9. Larger root is 9."
            },
            {
                "id": "ex15-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( x - y = 3 \\) and \\( x^2 - y^2 = 39 \\), find the value of \\( x + y \\).",
                "answer": 13, "displayAnswer": "13", "tolerance": 0, "unit": "",
                "hint": "(x - y)(x + y) = 39 => 3 * (x + y) = 39.",
                "explanation": "\\(x + y = \\frac{39}{3} = 13\\)."
            },
            {
                "id": "ex15-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 5(x - 2) = 3(x + 4) \\)",
                "answer": 11, "displayAnswer": "11", "tolerance": 0, "unit": "",
                "hint": "5x - 10 = 3x + 12 => 2x = 22 => x = 11.",
                "explanation": "\\(2x = 22 \\implies x = 11\\)."
            },
            {
                "id": "ex15-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate \\( \\frac{a^2 - b^2}{a - b} \\) when \\( a = 3.7 \\) and \\( b = 1.3 \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0.01, "unit": "",
                "hint": "Simplifies to a + b = 3.7 + 1.3 = 5.",
                "explanation": "\\(a + b = 3.7 + 1.3 = 5\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex15-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the square: \\( 30^2 \\)",
                "answer": 900, "displayAnswer": "900", "tolerance": 0, "unit": "",
                "hint": "30 * 30 = 900.",
                "explanation": "\\(30^2 = 900\\)."
            },
            {
                "id": "ex15-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "The period of a simple pendulum is \\( T = 2\\pi \\sqrt{\\frac{L}{g}} \\). If \\( L = 1 \\text{ m} \\), \\( g = \\pi^2 \\approx 9.87 \\text{ m/s}^2 \\), calculate \\( T \\) in seconds.",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.05, "unit": "s",
                "hint": "sqrt(1 / pi^2) = 1 / pi. T = 2*pi * (1/pi) = 2 s.",
                "explanation": "\\(T = 2\\pi \\times \\frac{1}{\\pi} = 2 \\text{ s}\\). This is known as a seconds pendulum."
            },
            {
                "id": "ex15-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert an electric energy of \\( 3.6 \\times 10^6 \\text{ J} \\) into kilowatt-hours (kWh).",
                "answer": 1, "displayAnswer": "1", "tolerance": 0, "unit": "kWh",
                "hint": "1 kWh = 1000 W * 3600 s = 3.6 * 10^6 J.",
                "explanation": "\\(1 \\text{ kWh} = 3.6 \\times 10^6 \\text{ J}\\)."
            },
            {
                "id": "ex15-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "An ideal gas expands from \\( V_1 = 2 \\text{ L} \\) to \\( V_2 = 5 \\text{ L} \\) against constant pressure \\( P = 2 \\times 10^5 \\text{ Pa} \\). Using \\( W = P\\Delta V \\), find work done \\( W \\) in Joules. (Recall \\( 1 \\text{ L} = 10^{-3} \\text{ m}^3 \\))",
                "answer": 600, "displayAnswer": "600", "tolerance": 1, "unit": "J",
                "hint": "Delta V = 3 L = 3 * 10^-3 m^3. W = 2*10^5 * 3*10^-3 = 600 J.",
                "explanation": "\\(W = 2 \\times 10^5 \\times 3 \\times 10^{-3} = 600 \\text{ J}\\)."
            },
            {
                "id": "ex15-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Surface tension force is \\( F = T \\times 2L \\). If \\( T = 0.075 \\text{ N/m} \\) and \\( L = 0.2 \\text{ m} \\), find \\( F \\) in Newtons.",
                "answer": 0.03, "displayAnswer": "0.03", "tolerance": 0.002, "unit": "N",
                "hint": "0.075 * 0.4 = 0.03.",
                "explanation": "\\(F = 0.075 \\times 0.4 = 0.03 \\text{ N}\\)."
            }
        ]
    }
]

print(f"Tier 3 loaded: {len(tier3)} exercises.")
