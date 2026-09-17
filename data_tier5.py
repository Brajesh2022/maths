# Tier 5: Exercises 21 - 25 (Advanced)

tier5 = [
    {
        "id": 21,
        "title": "Advanced: Capacitance & Surd Rationalization",
        "subtitle": "Parallel plate capacitance C = ε₀A/d, series/parallel capacitors, and surd algebra.",
        "difficulty": 5,
        "tier": "Advanced",
        "estimatedMinutes": 22,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex21-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{\\sqrt{3} - 1} \\) to 2 decimal places. (\\( \\frac{\\sqrt{3}+1}{2} \\))",
                "answer": 1.37, "displayAnswer": "1.37", "tolerance": 0.03, "unit": "",
                "hint": "(1.732 + 1) / 2 = 2.732 / 2 = 1.366 ≈ 1.37.",
                "explanation": "\\(\\frac{\\sqrt{3} + 1}{2} \\approx 1.366 \\approx 1.37\\)."
            },
            {
                "id": "ex21-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Two capacitors of \\( 6 \\text{ }\\mu\\text{F} \\) and \\( 3 \\text{ }\\mu\\text{F} \\) are connected in series. Find equivalent capacitance in \\( \\mu\\text{F} \\).",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "µF",
                "hint": "(6 * 3) / (6 + 3) = 18 / 9 = 2.",
                "explanation": "\\(C_s = \\frac{18}{9} = 2 \\text{ }\\mu\\text{F}\\)."
            },
            {
                "id": "ex21-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\frac{1.732}{2} + 0.134 \\)",
                "answer": 1, "displayAnswer": "1", "tolerance": 0.01, "unit": "",
                "hint": "0.866 + 0.134 = 1.000.",
                "explanation": "\\(0.866 + 0.134 = 1\\)."
            },
            {
                "id": "ex21-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 1.25 \\times 10^3 \\times 0.008 \\)",
                "answer": 10, "displayAnswer": "10", "tolerance": 0.01, "unit": "",
                "hint": "1250 * 0.008 = 10.",
                "explanation": "\\(1250 \\times 0.008 = 10\\)."
            },
            {
                "id": "ex21-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\sqrt{18} + \\sqrt{32} - \\sqrt{50} \\). Enter decimal value.",
                "answer": 2.83, "displayAnswer": "2.83 (or 2√2)", "tolerance": 0.05, "unit": "",
                "hint": "3*sqrt(2) + 4*sqrt(2) - 5*sqrt(2) = 2*sqrt(2) ≈ 2 * 1.414 = 2.828.",
                "explanation": "\\(2\\sqrt{2} \\approx 2.83\\)."
            },
            # Algebra (5)
            {
                "id": "ex21-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify the algebraic fraction \\( \\frac{1}{x-1} - \\frac{1}{x+1} \\) at \\( x = 3 \\). Enter decimal value.",
                "answer": 0.25, "displayAnswer": "0.25 (or 1/4)", "tolerance": 0.01, "unit": "",
                "hint": "2 / (x^2 - 1) = 2 / (9 - 1) = 2/8 = 0.25.",
                "explanation": "\\(\\frac{2}{x^2 - 1} = \\frac{2}{8} = 0.25\\)."
            },
            {
                "id": "ex21-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\frac{x}{x-2} + \\frac{x-2}{x} = \\frac{10}{3} \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0.01, "unit": "",
                "hint": "Let y = x/(x-2). y + 1/y = 10/3 => y = 3. x/(x-2) = 3 => x = 3x - 6 => 2x = 6 => x = 3.",
                "explanation": "\\(x = 3\\)."
            },
            {
                "id": "ex21-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\alpha, \\beta \\) are roots of \\( x^2 - 7x + 12 = 0 \\), what is \\( \\frac{1}{\\alpha} + \\frac{1}{\\beta} \\)? Enter as decimal to 3 decimal places.",
                "answer": 0.583, "displayAnswer": "0.583 (or 7/12)", "tolerance": 0.01, "unit": "",
                "hint": "(alpha + beta) / (alpha * beta) = 7 / 12 ≈ 0.583.",
                "explanation": "\\(\\frac{\\alpha+\\beta}{\\alpha\\beta} = \\frac{7}{12} \\approx 0.583\\)."
            },
            {
                "id": "ex21-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 3^{x+1} + 3^{x} = 36 \\)",
                "answer": 2, "displayAnswer": "2", "tolerance": 0, "unit": "",
                "hint": "3^x(3 + 1) = 4 * 3^x = 36 => 3^x = 9 => x = 2.",
                "explanation": "\\(4 \\times 3^x = 36 \\implies 3^x = 9 \\implies x = 2\\)."
            },
            {
                "id": "ex21-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate \\( \\frac{x^3 + 27}{x + 3} \\) at \\( x = 7 \\).",
                "answer": 37, "displayAnswer": "37", "tolerance": 0, "unit": "",
                "hint": "x^2 - 3x + 9 = 49 - 21 + 9 = 37.",
                "explanation": "\\(49 - 21 + 9 = 37\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex21-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Capacitance of a parallel plate capacitor is \\( C = \\frac{\\varepsilon_0 A}{d} \\). If \\( A = 0.02 \\text{ m}^2 \\), \\( d = 1.77 \\text{ mm} = 1.77 \\times 10^{-3} \\text{ m} \\), and \\( \\varepsilon_0 = 8.85 \\times 10^{-12} \\text{ F/m} \\), calculate \\( C \\) in pico-Farads (pF).",
                "answer": 100, "displayAnswer": "100", "tolerance": 2, "unit": "pF",
                "hint": "(8.85*10^-12 * 2*10^-2) / (1.77*10^-3) = (17.7 / 1.77) * 10^-11 = 10 * 10^-11 = 10^-10 F = 100 pF.",
                "explanation": "\\(C = 100 \\text{ pF}\\)."
            },
            {
                "id": "ex21-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A dielectric slab of \\( K = 4 \\) is inserted into a capacitor of capacitance \\( 25 \\text{ }\\mu\\text{F} \\). What is the new capacitance in \\( \\mu\\text{F} \\)?",
                "answer": 100, "displayAnswer": "100", "tolerance": 0, "unit": "µF",
                "hint": "C' = K * C = 4 * 25 = 100.",
                "explanation": "\\(C' = 4 \\times 25 = 100 \\text{ }\\mu\\text{F}\\)."
            },
            {
                "id": "ex21-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Two charges \\( q_1 = +2 \\text{ }\\mu\\text{C} \\) and \\( q_2 = +8 \\text{ }\\mu\\text{C} \\) are separated by distance \\( r = 0.6 \\text{ m} \\). Using \\( F = \\frac{k q_1 q_2}{r^2} \\) where \\( k = 9 \\times 10^9 \\), calculate force \\( F \\) in Newtons.",
                "answer": 0.4, "displayAnswer": "0.4", "tolerance": 0.01, "unit": "N",
                "hint": "9*10^9 * 16*10^-12 / 0.36 = 144*10^-3 / 0.36 = 0.144 / 0.36 = 0.4 N.",
                "explanation": "\\(F = \\frac{144 \\times 10^{-3}}{0.36} = 0.4 \\text{ N}\\)."
            },
            {
                "id": "ex21-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "At what distance from \\( q_1 = 1 \\text{ }\\mu\\text{C} \\) along the line to \\( q_2 = 9 \\text{ }\\mu\\text{C} \\) (separated by \\( 40 \\text{ cm} \\)) is the net electric field zero? (\\( x = \\frac{d}{1 + \\sqrt{q_2/q_1}} \\)) Enter in cm.",
                "answer": 10, "displayAnswer": "10", "tolerance": 0.1, "unit": "cm",
                "hint": "x = 40 / (1 + sqrt(9/1)) = 40 / (1 + 3) = 40 / 4 = 10 cm.",
                "explanation": "\\(x = \\frac{40}{1 + 3} = 10 \\text{ cm}\\)."
            },
            {
                "id": "ex21-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Energy density of electric field is \\( u = \\frac{1}{2}\\varepsilon_0 E^2 \\). If \\( E = 2000 \\text{ V/m} \\) and \\( \\varepsilon_0 = 8.85 \\times 10^{-12} \\text{ C}^2/(\\text{N}\\cdot\\text{m}^2) \\), calculate \\( u \\times 10^6 \\text{ J/m}^3 \\) (in micro-Joules per cubic meter).",
                "answer": 17.7, "displayAnswer": "17.7", "tolerance": 0.2, "unit": "µJ/m³",
                "hint": "0.5 * 8.85*10^-12 * 4*10^6 = 17.7 * 10^-6 J/m^3.",
                "explanation": "\\(u = 17.7 \\times 10^{-6} \\text{ J/m}^3 = 17.7 \\text{ }\\mu\\text{J/m}^3\\)."
            }
        ]
    },
    {
        "id": 22,
        "title": "Advanced: Photoelectric Equation & Modern Physics",
        "subtitle": "Master Einstein's photoelectric formula, stopping potential, and de Broglie electron relations.",
        "difficulty": 5,
        "tier": "Advanced",
        "estimatedMinutes": 22,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex22-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 3.1416 \\times 25 \\)",
                "answer": 78.54, "displayAnswer": "78.54", "tolerance": 0.2, "unit": "",
                "hint": "pi * 100 / 4 = 314.16 / 4 = 78.54.",
                "explanation": "\\(3.1416 \\times 25 = 78.54\\)."
            },
            {
                "id": "ex22-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1240}{400} \\). (Shortcut for photon energy at 400 nm)",
                "answer": 3.1, "displayAnswer": "3.1", "tolerance": 0.02, "unit": "eV",
                "hint": "124 / 40 = 3.1.",
                "explanation": "\\(1240 / 400 = 3.1 \\text{ eV}\\)."
            },
            {
                "id": "ex22-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "If work function \\( \\Phi = 2.1 \\text{ eV} \\) and incident photon energy \\( E = 3.1 \\text{ eV} \\), find maximum kinetic energy \\( K_{\\text{max}} = E - \\Phi \\) in eV.",
                "answer": 1, "displayAnswer": "1", "tolerance": 0, "unit": "eV",
                "hint": "3.1 - 2.1 = 1.0 eV.",
                "explanation": "\\(K_{\\text{max}} = 3.1 - 2.1 = 1.0 \\text{ eV}\\)."
            },
            {
                "id": "ex22-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "What is stopping potential \\( V_0 \\) in Volts if \\( K_{\\text{max}} = 1.0 \\text{ eV} \\)?",
                "answer": 1, "displayAnswer": "1", "tolerance": 0, "unit": "V",
                "hint": "e * V_0 = 1.0 eV => V_0 = 1.0 V.",
                "explanation": "\\(V_0 = 1.0 \\text{ V}\\)."
            },
            {
                "id": "ex22-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\sqrt{\\frac{150}{150}} \\times 1.227 \\) (de Broglie formula for electron: \\( \\lambda = \\frac{12.27}{\\sqrt{V}} \\text{ \\AA} \\) at \\( V = 100 \\text{ V} \\)). What is \\( \\lambda \\) in \\( \\text{\\AA} \\)?",
                "answer": 1.227, "displayAnswer": "1.227", "tolerance": 0.05, "unit": "Å",
                "hint": "12.27 / sqrt(100) = 12.27 / 10 = 1.227 Å.",
                "explanation": "\\(\\lambda = \\frac{12.27}{10} = 1.227 \\text{ \\AA}\\)."
            },
            # Algebra (5)
            {
                "id": "ex22-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( \\lambda \\): \\( \\frac{1240}{\\lambda} - 2.0 = 3.0 \\). Enter \\( \\lambda \\) in nm.",
                "answer": 248, "displayAnswer": "248", "tolerance": 1, "unit": "nm",
                "hint": "1240 / lambda = 5.0 => lambda = 1240 / 5 = 248 nm.",
                "explanation": "\\(\\lambda = \\frac{1240}{5} = 248 \\text{ nm}\\)."
            },
            {
                "id": "ex22-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( v \\): \\( \\frac{1}{2}(9.1 \\times 10^{-31}) v^2 = 1.6 \\times 10^{-19} \\times 4.55 \\). What is \\( v \\times 10^{-6} \\text{ m/s} \\)?",
                "answer": 1.26, "displayAnswer": "1.26 (v ≈ 1.26×10⁶ m/s)", "tolerance": 0.1, "unit": "",
                "hint": "v^2 = 2 * (1.6 * 4.55 / 9.1) * 10^12 = 2 * (1.6 * 0.5) * 10^12 = 1.6 * 10^12 => v = sqrt(1.6)*10^6 ≈ 1.265 * 10^6.",
                "explanation": "\\(v = \\sqrt{1.6} \\times 10^6 \\approx 1.265 \\times 10^6 \\text{ m/s}\\)."
            },
            {
                "id": "ex22-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{x^2 - y^2}{(x - y)^2} \\) when \\( x = 3.5 \\) and \\( y = 1.5 \\).",
                "answer": 2.5, "displayAnswer": "2.5 (or 5/2)", "tolerance": 0.01, "unit": "",
                "hint": "(x + y)/(x - y) = (3.5 + 1.5) / (3.5 - 1.5) = 5.0 / 2.0 = 2.5.",
                "explanation": "\\(\\frac{5}{2} = 2.5\\)."
            },
            {
                "id": "ex22-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\log_{10}(2) = 0.3010 \\), what is \\( \\log_{10}(8) \\) to 3 decimal places?",
                "answer": 0.903, "displayAnswer": "0.903", "tolerance": 0.005, "unit": "",
                "hint": "log(2^3) = 3 * log(2) = 3 * 0.3010 = 0.903.",
                "explanation": "\\(3 \\times 0.3010 = 0.903\\)."
            },
            {
                "id": "ex22-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the half-life multiplier: \\( \\ln 2 \\approx 0.693 \\). If decay constant \\( \\lambda = 0.0693 \\text{ s}^{-1} \\), what is half-life \\( T_{1/2} = \\frac{0.693}{\\lambda} \\) in seconds?",
                "answer": 10, "displayAnswer": "10", "tolerance": 0.05, "unit": "s",
                "hint": "0.693 / 0.0693 = 10.",
                "explanation": "\\(T_{1/2} = \\frac{0.693}{0.0693} = 10 \\text{ s}\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex22-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Threshold wavelength of a metal is \\( \\lambda_0 = 620 \\text{ nm} \\). Calculate work function \\( \\Phi = \\frac{1240}{\\lambda_0} \\) in eV.",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "eV",
                "hint": "1240 / 620 = 2 eV.",
                "explanation": "\\(\\Phi = 2 \\text{ eV}\\)."
            },
            {
                "id": "ex22-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "If a metal with work function \\( 2.5 \\text{ eV} \\) is illuminated with light of photon energy \\( 4.0 \\text{ eV} \\), find the stopping potential \\( V_0 \\) in Volts.",
                "answer": 1.5, "displayAnswer": "1.5", "tolerance": 0.01, "unit": "V",
                "hint": "V_0 = (4.0 - 2.5) = 1.5 V.",
                "explanation": "\\(V_0 = 4.0 - 2.5 = 1.5 \\text{ V}\\)."
            },
            {
                "id": "ex22-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "In a nuclear reaction, mass defect is \\( \\Delta m = 0.02 \\text{ amu} \\). Calculate energy released in MeV. (Recall \\( 1 \\text{ amu} = 931.5 \\text{ MeV} \\))",
                "answer": 18.63, "displayAnswer": "18.63", "tolerance": 0.2, "unit": "MeV",
                "hint": "0.02 * 931.5 = 18.63 MeV.",
                "explanation": "\\(0.02 \\times 931.5 = 18.63 \\text{ MeV}\\)."
            },
            {
                "id": "ex22-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Activity of a radioactive sample drops to \\( 1/16 \\) of initial activity in \\( 20 \\text{ minutes} \\). Find the half-life in minutes. (\\( (1/2)^n = 1/16 \\implies n = 4 \\))",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "min",
                "hint": "4 half lives in 20 minutes => 20 / 4 = 5 min.",
                "explanation": "\\(T_{1/2} = \\frac{20}{4} = 5 \\text{ minutes}\\)."
            },
            {
                "id": "ex22-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "The fraction of radioactive nuclei remaining after 3 half-lives is \\( (1/2)^3 \\). Enter as decimal.",
                "answer": 0.125, "displayAnswer": "0.125 (or 1/8)", "tolerance": 0.005, "unit": "",
                "hint": "1 / 8 = 0.125.",
                "explanation": "\\((1/2)^3 = \\frac{1}{8} = 0.125\\)."
            }
        ]
    },
    {
        "id": 23,
        "title": "Advanced: Rapid Approximation Under Time Pressure",
        "subtitle": "Master NEET/JEE mental shortcuts: π² ≈ 10, g ≈ 9.8 or 10, e ≈ 2.718, and small-angle approximations.",
        "difficulty": 5,
        "tier": "Advanced",
        "estimatedMinutes": 22,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex23-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Using \\( \\pi^2 \\approx 9.87 \\approx 10 \\), evaluate: \\( \\frac{40}{\\pi^2} \\)",
                "answer": 4, "displayAnswer": "4 (approx 4.05)", "tolerance": 0.2, "unit": "",
                "hint": "40 / 10 = 4.",
                "explanation": "\\(40 / 10 = 4\\)."
            },
            {
                "id": "ex23-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\frac{1}{0.98} \\) using binomial approximation \\( (1 - x)^{-1} \\approx 1 + x \\).",
                "answer": 1.02, "displayAnswer": "1.02", "tolerance": 0.005, "unit": "",
                "hint": "1 / (1 - 0.02) ≈ 1 + 0.02 = 1.02.",
                "explanation": "\\((1 - 0.02)^{-1} \\approx 1 + 0.02 = 1.02\\)."
            },
            {
                "id": "ex23-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( (1.02)^5 \\approx 1 + 5(0.02) \\). Enter decimal value.",
                "answer": 1.1, "displayAnswer": "1.10", "tolerance": 0.01, "unit": "",
                "hint": "1 + 0.10 = 1.10.",
                "explanation": "\\(1 + 5 \\times 0.02 = 1.10\\)."
            },
            {
                "id": "ex23-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Estimate: \\( \\sqrt{101} \\approx 10 + \\frac{1}{20} \\). Enter as decimal.",
                "answer": 10.05, "displayAnswer": "10.05", "tolerance": 0.02, "unit": "",
                "hint": "sqrt(100 + 1) ≈ 10 * (1 + 1/200) = 10 + 0.05 = 10.05.",
                "explanation": "\\(\\sqrt{101} \\approx 10.05\\)."
            },
            {
                "id": "ex23-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 18.5 \\times 4.2 \\) to 1 decimal place.",
                "answer": 77.7, "displayAnswer": "77.7", "tolerance": 0.5, "unit": "",
                "hint": "18.5 * 4 = 74; 18.5 * 0.2 = 3.7. 74 + 3.7 = 77.7.",
                "explanation": "\\(74 + 3.7 = 77.7\\)."
            },
            # Algebra (5)
            {
                "id": "ex23-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If percentage error in measuring radius \\( r \\) is \\( 2\\% \\), what is the percentage error in measuring sphere surface area \\( A = 4\\pi r^2 \\)? (\\( \\% \\text{ error} = 2 \\times \\% \\Delta r \\))",
                "answer": 4, "displayAnswer": "4%", "tolerance": 0, "unit": "%",
                "hint": "Power is 2 => 2 * 2% = 4%.",
                "explanation": "\\(2 \\times 2\\% = 4\\%\\)."
            },
            {
                "id": "ex23-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "What is the percentage error in volume \\( V = \\frac{4}{3}\\pi r^3 \\) if radius error is \\( 2\\% \\)?",
                "answer": 6, "displayAnswer": "6%", "tolerance": 0, "unit": "%",
                "hint": "3 * 2% = 6%.",
                "explanation": "\\(3 \\times 2\\% = 6\\%\\)."
            },
            {
                "id": "ex23-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "In \\( T = 2\\pi \\sqrt{\\frac{L}{g}} \\), if \\( L \\) has \\( 2\\% \\) error and \\( g \\) has \\( 1\\% \\) error, what is maximum percentage error in \\( T \\)? (\\( \\frac{1}{2}(\\%L + \\%g) \\))",
                "answer": 1.5, "displayAnswer": "1.5%", "tolerance": 0.01, "unit": "%",
                "hint": "0.5 * (2% + 1%) = 0.5 * 3% = 1.5%.",
                "explanation": "\\(0.5 \\times 3\\% = 1.5\\%\\)."
            },
            {
                "id": "ex23-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( (x + 0.1)^2 \\approx x^2 + 0.2x = 4.41 \\) where \\( x = 2 \\). Verify: \\( 2.1^2 \\). What is \\( 2.1^2 \\)?",
                "answer": 4.41, "displayAnswer": "4.41", "tolerance": 0.01, "unit": "",
                "hint": "21^2 = 441 => 4.41.",
                "explanation": "\\(2.1^2 = 4.41\\)."
            },
            {
                "id": "ex23-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{2x}{x+3} = 1.6 \\)",
                "answer": 12, "displayAnswer": "12", "tolerance": 0.1, "unit": "",
                "hint": "2x = 1.6x + 4.8 => 0.4x = 4.8 => x = 12.",
                "explanation": "\\(0.4x = 4.8 \\implies x = 12\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex23-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Speed of sound in air is \\( v = 340 \\text{ m/s} \\). A tuning fork has frequency \\( f = 512 \\text{ Hz} \\). Using \\( \\lambda = \\frac{v}{f} \\), calculate wavelength \\( \\lambda \\) in meters to 2 decimal places.",
                "answer": 0.66, "displayAnswer": "0.66", "tolerance": 0.03, "unit": "m",
                "hint": "340 / 512 ≈ 340 / 510 = 34/51 = 2/3 ≈ 0.667 m.",
                "explanation": "\\(\\lambda = \\frac{340}{512} \\approx 0.664 \\text{ m}\\)."
            },
            {
                "id": "ex23-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A lens has focal length \\( f = +20 \\text{ cm} = +0.2 \\text{ m} \\). What is its optical power \\( P = \\frac{1}{f \\text{ (in m)}} \\) in Dioptres (D)?",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "D",
                "hint": "1 / 0.2 = 5 D.",
                "explanation": "\\(P = \\frac{1}{0.2} = +5 \\text{ D}\\)."
            },
            {
                "id": "ex23-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Two thin lenses of powers \\( +5 \\text{ D} \\) and \\( -2 \\text{ D} \\) are placed in contact. What is the combination power \\( P_{\\text{eq}} = P_1 + P_2 \\) in Dioptres?",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "D",
                "hint": "5 - 2 = 3 D.",
                "explanation": "\\(P_{\\text{eq}} = 5 - 2 = +3 \\text{ D}\\)."
            },
            {
                "id": "ex23-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the equivalent focal length \\( f_{\\text{eq}} \\) in cm of this combination (\\( P = 3 \\text{ D} \\))? Enter to 1 decimal place. (\\( f = \\frac{100}{P} \\text{ cm} \\))",
                "answer": 33.3, "displayAnswer": "33.3", "tolerance": 0.5, "unit": "cm",
                "hint": "100 / 3 = 33.33 cm.",
                "explanation": "\\(f = \\frac{100}{3} \\approx 33.3 \\text{ cm}\\)."
            },
            {
                "id": "ex23-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Magnetic field at center of circular coil of radius \\( R = 0.1 \\text{ m} \\) carrying current \\( I = 5 \\text{ A} \\) is \\( B = \\frac{\\mu_0 I}{2R} \\). If \\( \\mu_0 = 4\\pi \\times 10^{-7} \\), calculate \\( B \\times 10^5 \\text{ T} \\). (Use \\( \\pi \\approx 3.14 \\))",
                "answer": 3.14, "displayAnswer": "3.14 (B = 3.14×10⁻⁵ T)", "tolerance": 0.1, "unit": "",
                "hint": "(4*pi*10^-7 * 5) / (2 * 0.1) = 20*pi*10^-7 / 0.2 = 100*pi*10^-7 = pi * 10^-5 T.",
                "explanation": "\\(B = \\pi \\times 10^{-5} \\text{ T} \\approx 3.14 \\times 10^{-5} \\text{ T}\\)."
            }
        ]
    },
    {
        "id": 24,
        "title": "Advanced: Rotational Dynamics & Moment of Inertia",
        "subtitle": "Calculate moments of inertia (MR²/2, 2MR²/5), angular momentum, and rotational kinetic energy.",
        "difficulty": 5,
        "tier": "Advanced",
        "estimatedMinutes": 22,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex24-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\frac{2}{5} \\times 2.5 \\)",
                "answer": 1, "displayAnswer": "1", "tolerance": 0, "unit": "",
                "hint": "0.4 * 2.5 = 1.",
                "explanation": "\\(0.4 \\times 2.5 = 1\\)."
            },
            {
                "id": "ex24-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 12^2 \\div 36 \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "144 / 36 = 4.",
                "explanation": "\\(144 / 36 = 4\\)."
            },
            {
                "id": "ex24-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( 0.5 \\times 4 \\times 15^2 \\)",
                "answer": 450, "displayAnswer": "450", "tolerance": 0, "unit": "",
                "hint": "2 * 225 = 450.",
                "explanation": "\\(2 \\times 225 = 450\\)."
            },
            {
                "id": "ex24-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 2\\pi \\times 50 \\). (Use \\( \\pi \\approx 3.14 \\))",
                "answer": 314, "displayAnswer": "314", "tolerance": 1, "unit": "",
                "hint": "100 * 3.14 = 314.",
                "explanation": "\\(100 \\times 3.14 = 314\\)."
            },
            {
                "id": "ex24-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\sqrt{\\frac{4900}{100}} \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "sqrt(49) = 7.",
                "explanation": "\\(\\sqrt{49} = 7\\)."
            },
            # Algebra (5)
            {
                "id": "ex24-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Moment of inertia of a disc is \\( I = \\frac{1}{2}MR^2 \\). If mass \\( M = 4 \\text{ kg} \\) and radius \\( R = 0.5 \\text{ m} \\), find \\( I \\) in \\( \\text{kg}\\cdot\\text{m}^2 \\).",
                "answer": 0.5, "displayAnswer": "0.5", "tolerance": 0.01, "unit": "kg·m²",
                "hint": "0.5 * 4 * 0.25 = 2 * 0.25 = 0.5.",
                "explanation": "\\(I = 0.5 \\times 4 \\times 0.25 = 0.5 \\text{ kg}\\cdot\\text{m}^2\\)."
            },
            {
                "id": "ex24-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "For a solid sphere, \\( I = \\frac{2}{5}MR^2 \\). If \\( M = 5 \\text{ kg} \\) and \\( R = 0.2 \\text{ m} \\), calculate \\( I \\) in \\( \\text{kg}\\cdot\\text{m}^2 \\).",
                "answer": 0.08, "displayAnswer": "0.08", "tolerance": 0.005, "unit": "kg·m²",
                "hint": "(2/5) * 5 * 0.04 = 2 * 0.04 = 0.08.",
                "explanation": "\\(I = 2 \\times 0.04 = 0.08 \\text{ kg}\\cdot\\text{m}^2\\)."
            },
            {
                "id": "ex24-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Rotational kinetic energy is \\( K_{\\text{rot}} = \\frac{1}{2}I\\omega^2 \\). If \\( I = 0.4 \\text{ kg}\\cdot\\text{m}^2 \\) and \\( \\omega = 10 \\text{ rad/s} \\), calculate \\( K_{\\text{rot}} \\) in Joules.",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "J",
                "hint": "0.5 * 0.4 * 100 = 0.2 * 100 = 20 J.",
                "explanation": "\\(K_{\\text{rot}} = 0.2 \\times 100 = 20 \\text{ J}\\)."
            },
            {
                "id": "ex24-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Angular momentum is \\( L = I\\omega \\). If \\( I = 2.5 \\text{ kg}\\cdot\\text{m}^2 \\) and \\( \\omega = 8 \\text{ rad/s} \\), find \\( L \\) in \\( \\text{J}\\cdot\\text{s} \\).",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "J·s",
                "hint": "2.5 * 8 = 20.",
                "explanation": "\\(L = 2.5 \\times 8 = 20 \\text{ J}\\cdot\\text{s}\\)."
            },
            {
                "id": "ex24-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( \\omega \\): \\( \\frac{1}{2}(0.5)\\omega^2 = 16 \\)",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "rad/s",
                "hint": "0.25 * omega^2 = 16 => omega^2 = 64 => omega = 8.",
                "explanation": "\\(\\omega^2 = 64 \\implies \\omega = 8 \\text{ rad/s}\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex24-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Radius of gyration \\( k \\) of a ring of radius \\( R = 10 \\text{ cm} \\) about its central axis is \\( k = R \\). What is \\( k \\) in cm?",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "cm",
                "hint": "For a thin ring, I = M R^2 = M k^2 => k = R = 10 cm.",
                "explanation": "\\(k = R = 10 \\text{ cm}\\)."
            },
            {
                "id": "ex24-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A torque of \\( \\tau = 12 \\text{ N}\\cdot\\text{m} \\) acts on a wheel with moment of inertia \\( I = 3 \\text{ kg}\\cdot\\text{m}^2 \\). Using \\( \\tau = I\\alpha \\), calculate angular acceleration \\( \\alpha \\) in \\( \\text{rad/s}^2 \\).",
                "answer": 4, "displayAnswer": "4", "tolerance": 0.01, "unit": "rad/s²",
                "hint": "alpha = tau / I = 12 / 3 = 4.",
                "explanation": "\\(\\alpha = \\frac{12}{3} = 4 \\text{ rad/s}^2\\)."
            },
            {
                "id": "ex24-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Starting from rest (\\( \\omega_0 = 0 \\)) with \\( \\alpha = 4 \\text{ rad/s}^2 \\), calculate angular speed \\( \\omega = \\omega_0 + \\alpha t \\) after \\( t = 5 \\text{ s} \\) in \\( \\text{rad/s} \\).",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "rad/s",
                "hint": "4 * 5 = 20.",
                "explanation": "\\(\\omega = 4 \\times 5 = 20 \\text{ rad/s}\\)."
            },
            {
                "id": "ex24-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the angle rotated in radians \\( \\theta = \\frac{1}{2}\\alpha t^2 \\) for \\( \\alpha = 4 \\text{ rad/s}^2 \\) and \\( t = 5 \\text{ s} \\).",
                "answer": 50, "displayAnswer": "50", "tolerance": 0, "unit": "rad",
                "hint": "0.5 * 4 * 25 = 50 rad.",
                "explanation": "\\(\\theta = 0.5 \\times 4 \\times 25 = 50 \\text{ radians}\\)."
            },
            {
                "id": "ex24-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Convert \\( 300 \\text{ rpm} \\) (revolutions per minute) to angular velocity \\( \\omega \\) in \\( \\text{rad/s} \\). Enter to 1 decimal place. (\\( \\omega = \\frac{2\\pi N}{60} \\approx \\frac{3.1416 \\times 300}{30} = 10\\pi \\))",
                "answer": 31.4, "displayAnswer": "31.4 (or 10π)", "tolerance": 0.5, "unit": "rad/s",
                "hint": "2*pi*300 / 60 = 10*pi ≈ 31.4 rad/s.",
                "explanation": "\\(\\omega = 10\\pi \\approx 31.42 \\text{ rad/s}\\)."
            }
        ]
    },
    {
        "id": 25,
        "title": "Advanced: Thermal Physics & Stefan's Law",
        "subtitle": "Calculate blackbody radiation P = σAT⁴, root mean square speed, and gas work.",
        "difficulty": 5,
        "tier": "Advanced",
        "estimatedMinutes": 22,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex25-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "If absolute temperature of a blackbody doubles from \\( T \\) to \\( 2T \\), by what factor does radiated power increase? (\\( P \\propto T^4 \\))",
                "answer": 16, "displayAnswer": "16", "tolerance": 0, "unit": "",
                "hint": "2^4 = 16.",
                "explanation": "\\(2^4 = 16\\)."
            },
            {
                "id": "ex25-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Convert temperature \\( 27^\\circ\\text{C} \\) to Kelvin. (\\( T = \\theta + 273 \\))",
                "answer": 300, "displayAnswer": "300", "tolerance": 0, "unit": "K",
                "hint": "27 + 273 = 300 K.",
                "explanation": "\\(27 + 273 = 300 \\text{ K}\\)."
            },
            {
                "id": "ex25-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Convert temperature \\( 127^\\circ\\text{C} \\) to Kelvin.",
                "answer": 400, "displayAnswer": "400", "tolerance": 0, "unit": "K",
                "hint": "127 + 273 = 400 K.",
                "explanation": "\\(127 + 273 = 400 \\text{ K}\\)."
            },
            {
                "id": "ex25-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate the ratio \\( \\left(\\frac{400}{300}\\right)^4 \\). Enter as decimal to 2 decimal places.",
                "answer": 3.16, "displayAnswer": "3.16 (or 256/81)", "tolerance": 0.05, "unit": "",
                "hint": "(4/3)^4 = 256 / 81 ≈ 3.16.",
                "explanation": "\\(\\frac{256}{81} \\approx 3.16\\)."
            },
            {
                "id": "ex25-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 8.314 \\times 300 \\) to nearest whole number.",
                "answer": 2494, "displayAnswer": "2494 (or 2494.2)", "tolerance": 5, "unit": "",
                "hint": "8.314 * 3 = 24.942 => * 100 = 2494.2.",
                "explanation": "\\(8.314 \\times 300 = 2494.2\\)."
            },
            # Algebra (5)
            {
                "id": "ex25-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Wien's Displacement Law is \\( \\lambda_m T = b \\). If \\( b = 2.9 \\times 10^{-3} \\text{ m}\\cdot\\text{K} \\) and \\( T = 5800 \\text{ K} \\) (Sun surface), find \\( \\lambda_m \\) in nanometers (nm).",
                "answer": 500, "displayAnswer": "500", "tolerance": 5, "unit": "nm",
                "hint": "(2.9 * 10^-3) / 5800 = (2.9 / 5.8) * 10^-6 = 0.5 * 10^-6 m = 500 nm.",
                "explanation": "\\(\\lambda_m = 500 \\text{ nm}\\)."
            },
            {
                "id": "ex25-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Root-mean-square speed of gas molecules is \\( v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}} \\). If temperature is quadrupled (\\( 4T \\)), by what factor does \\( v_{\\text{rms}} \\) increase?",
                "answer": 2, "displayAnswer": "2", "tolerance": 0, "unit": "",
                "hint": "sqrt(4) = 2.",
                "explanation": "\\(\\sqrt{4} = 2\\)."
            },
            {
                "id": "ex25-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( T_2 \\) in adiabatic relation \\( T_1 V_1^{\\gamma - 1} = T_2 V_2^{\\gamma - 1} \\). For a monatomic gas (\\( \\gamma = 5/3 \\)), \\( \\gamma - 1 = 2/3 \\). If \\( T_1 = 300 \\text{ K} \\) and volume is compressed to \\( V_2 = \\frac{1}{8}V_1 \\), find \\( T_2 \\) in Kelvin.",
                "answer": 1200, "displayAnswer": "1200", "tolerance": 10, "unit": "K",
                "hint": "T2 = 300 * (8)^(2/3) = 300 * 4 = 1200 K.",
                "explanation": "\\(T_2 = 300 \\times (8)^{2/3} = 300 \\times 4 = 1200 \\text{ K}\\)."
            },
            {
                "id": "ex25-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Efficiency of a Carnot engine is \\( \\eta = 1 - \\frac{T_C}{T_H} \\). If \\( T_H = 500 \\text{ K} \\) and \\( T_C = 300 \\text{ K} \\), find efficiency \\( \\eta \\) as percentage (%).",
                "answer": 40, "displayAnswer": "40%", "tolerance": 0.1, "unit": "%",
                "hint": "1 - 300/500 = 1 - 0.6 = 0.4 = 40%.",
                "explanation": "\\(\\eta = 1 - 0.6 = 0.4 = 40\\%\\)."
            },
            {
                "id": "ex25-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If Carnot engine absorbs \\( Q_H = 1000 \\text{ J} \\) at \\( \\eta = 40\\% \\), calculate useful work done \\( W = \\eta Q_H \\) in Joules.",
                "answer": 400, "displayAnswer": "400", "tolerance": 0, "unit": "J",
                "hint": "0.4 * 1000 = 400 J.",
                "explanation": "\\(W = 0.4 \\times 1000 = 400 \\text{ J}\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex25-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Heat rejected by the above engine to the sink is \\( Q_C = Q_H - W \\). Calculate \\( Q_C \\) in Joules.",
                "answer": 600, "displayAnswer": "600", "tolerance": 0, "unit": "J",
                "hint": "1000 - 400 = 600 J.",
                "explanation": "\\(Q_C = 1000 - 400 = 600 \\text{ J}\\)."
            },
            {
                "id": "ex25-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate total kinetic energy of 1 mole of monoatomic gas at \\( T = 300 \\text{ K} \\): \\( E = \\frac{3}{2}RT \\). (Use \\( R = 8.314 \\text{ J/(mol}\\cdot\\text{K)} \\)) Enter to nearest integer.",
                "answer": 3741, "displayAnswer": "3741", "tolerance": 10, "unit": "J",
                "hint": "1.5 * 8.314 * 300 = 1.5 * 2494.2 = 3741.3 J.",
                "explanation": "\\(E = 1.5 \\times 8.314 \\times 300 \\approx 3741 \\text{ J}\\)."
            },
            {
                "id": "ex25-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Latent heat of fusion of ice is \\( L_f = 3.36 \\times 10^5 \\text{ J/kg} \\). Calculate heat required \\( Q = mL_f \\) to melt \\( 50 \\text{ g} = 0.05 \\text{ kg} \\) of ice at \\( 0^\\circ\\text{C} \\) in Joules.",
                "answer": 16800, "displayAnswer": "16800", "tolerance": 20, "unit": "J",
                "hint": "0.05 * 336000 = 16800 J.",
                "explanation": "\\(Q = 0.05 \\times 3.36 \\times 10^5 = 16,800 \\text{ J}\\)."
            },
            {
                "id": "ex25-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Rate of heat conduction is \\( \\frac{dQ}{dt} = \\frac{KA(T_1 - T_2)}{L} \\). If thermal conductivity \\( K = 400 \\text{ W/(m}\\cdot\\text{K)} \\), area \\( A = 0.01 \\text{ m}^2 \\), \\( \\Delta T = 50 \\text{ K} \\), and length \\( L = 0.2 \\text{ m} \\), find \\( \\frac{dQ}{dt} \\) in Watts.",
                "answer": 1000, "displayAnswer": "1000", "tolerance": 5, "unit": "W",
                "hint": "(400 * 0.01 * 50) / 0.2 = 200 / 0.2 = 1000 W.",
                "explanation": "\\(\\frac{dQ}{dt} = \\frac{200}{0.2} = 1000 \\text{ W}\\)."
            },
            {
                "id": "ex25-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A body cools from \\( 80^\\circ\\text{C} \\) to \\( 60^\\circ\\text{C} \\) in \\( 5 \\text{ minutes} \\) with surrounding at \\( 20^\\circ\\text{C} \\). Average temp is \\( 70^\\circ\\text{C} \\), excess temp is \\( 50^\\circ\\text{C} \\). Rate of cooling \\( \\frac{dT}{dt} = \\frac{20}{5} = 4^\\circ\\text{C/min} \\). What is cooling constant \\( k = \\frac{4}{50} \\text{ min}^{-1} \\)? Enter as decimal.",
                "answer": 0.08, "displayAnswer": "0.08", "tolerance": 0.005, "unit": "min⁻¹",
                "hint": "4 / 50 = 8 / 100 = 0.08.",
                "explanation": "\\(k = \\frac{4}{50} = 0.08 \\text{ min}^{-1}\\)."
            }
        ]
    }
]

print(f"Tier 5 loaded: {len(tier5)} exercises.")
