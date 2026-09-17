# Tier 4: Exercises 16 - 20 (Intermediate -> Advanced)

tier4 = [
    {
        "id": 16,
        "title": "Intermediate → Advanced: Fundamental Constants & Powers of 10",
        "subtitle": "Manipulate Planck's constant, electronic charge, and fractional exponents.",
        "difficulty": 4,
        "tier": "Intermediate → Advanced",
        "estimatedMinutes": 20,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex16-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( 8^{2/3} \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "(8^(1/3))^2 = 2^2 = 4.",
                "explanation": "\\((8^{1/3})^2 = 2^2 = 4\\)."
            },
            {
                "id": "ex16-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( 16^{-3/4} \\). Enter as decimal.",
                "answer": 0.125, "displayAnswer": "0.125 (or 1/8)", "tolerance": 0.005, "unit": "",
                "hint": "1 / (16^(1/4))^3 = 1 / 2^3 = 1/8 = 0.125.",
                "explanation": "\\(\\frac{1}{2^3} = \\frac{1}{8} = 0.125\\)."
            },
            {
                "id": "ex16-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 125 \\times 0.032 \\)",
                "answer": 4, "displayAnswer": "4", "tolerance": 0.01, "unit": "",
                "hint": "125 * 32 = 4000. Shift 3 decimal places = 4.",
                "explanation": "\\(125 \\times 0.032 = 4\\)."
            },
            {
                "id": "ex16-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 3.2 \\times 10^{-19} \\div (1.6 \\times 10^{-19}) \\)",
                "answer": 2, "displayAnswer": "2", "tolerance": 0, "unit": "",
                "hint": "Ratio of charges: 3.2 / 1.6 = 2.",
                "explanation": "\\(3.2 / 1.6 = 2\\)."
            },
            {
                "id": "ex16-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( (2.5)^2 + (1.5)^2 \\)",
                "answer": 8.5, "displayAnswer": "8.5", "tolerance": 0.01, "unit": "",
                "hint": "6.25 + 2.25 = 8.50.",
                "explanation": "\\(6.25 + 2.25 = 8.50\\)."
            },
            # Algebra (5)
            {
                "id": "ex16-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 2^{2x - 1} = 32 \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "32 = 2^5. 2x - 1 = 5 => 2x = 6 => x = 3.",
                "explanation": "\\(2x - 1 = 5 \\implies 2x = 6 \\implies x = 3\\)."
            },
            {
                "id": "ex16-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Simplify \\( \\frac{x^2 - 5x + 6}{x - 2} \\) at \\( x = 10 \\).",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "(x - 2)(x - 3)/(x - 2) = x - 3. At x = 10: 10 - 3 = 7.",
                "explanation": "\\(10 - 3 = 7\\)."
            },
            {
                "id": "ex16-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\log_{10}(x) = 3 \\), what is the value of \\( \\frac{x}{200} \\)?",
                "answer": 5, "displayAnswer": "5", "tolerance": 0, "unit": "",
                "hint": "x = 10^3 = 1000. 1000 / 200 = 5.",
                "explanation": "\\(x = 1000 \\implies \\frac{1000}{200} = 5\\)."
            },
            {
                "id": "ex16-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the positive root of \\( 3x^2 - 14x - 5 = 0 \\).",
                "answer": 5, "displayAnswer": "5 (roots are -1/3, 5)", "tolerance": 0.01, "unit": "",
                "hint": "(3x + 1)(x - 5) = 0.",
                "explanation": "\\((3x+1)(x-5) = 0\\). Positive root is 5."
            },
            {
                "id": "ex16-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( x = \\sqrt{7 + 4\\sqrt{3}} \\), evaluate \\( x - \\frac{1}{x} \\). (Recall \\( 7 + 4\\sqrt{3} = (2 + \\sqrt{3})^2 \\)) Enter as decimal.",
                "answer": 3.46, "displayAnswer": "3.46 (or 2√3)", "tolerance": 0.05, "unit": "",
                "hint": "x = 2 + sqrt(3). 1/x = 2 - sqrt(3). x - 1/x = 2*sqrt(3) ≈ 2 * 1.732 = 3.464.",
                "explanation": "\\((2+\\sqrt{3}) - (2-\\sqrt{3}) = 2\\sqrt{3} \\approx 3.464\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex16-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Energy of a photon is \\( E = \\frac{hc}{\\lambda} \\). In eV, \\( E \\approx \\frac{1240}{\\lambda \\text{ (in nm)}} \\). If \\( \\lambda = 620 \\text{ nm} \\), calculate photon energy \\( E \\) in eV.",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "eV",
                "hint": "1240 / 620 = 2.",
                "explanation": "\\(E = \\frac{1240}{620} = 2 \\text{ eV}\\). Memorize 1240 nm·eV shortcut for NEET/JEE modern physics!"
            },
            {
                "id": "ex16-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the de Broglie wavelength multiplier: \\( \\lambda = \\frac{h}{p} \\). If \\( h = 6.63 \\times 10^{-34} \\text{ J}\\cdot\\text{s} \\) and momentum \\( p = 2.21 \\times 10^{-24} \\text{ kg}\\cdot\\text{m/s} \\), what is \\( \\lambda \\times 10^{10} \\text{ m} \\)? (In Angstroms)",
                "answer": 3, "displayAnswer": "3 (λ = 3 Å = 3×10⁻¹⁰ m)", "tolerance": 0.05, "unit": "Å",
                "hint": "6.63 / 2.21 = 3. -34 - (-24) = -10.",
                "explanation": "\\(\\lambda = 3 \\times 10^{-10} \\text{ m} = 3 \\text{ \\AA}\\)."
            },
            {
                "id": "ex16-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the magnitude of resultant of two perpendicular vectors \\( A = 12 \\) and \\( B = 5 \\): \\( R = \\sqrt{A^2 + B^2} \\).",
                "answer": 13, "displayAnswer": "13", "tolerance": 0, "unit": "",
                "hint": "5-12-13 Pythagorean triple. sqrt(144 + 25) = sqrt(169) = 13.",
                "explanation": "\\(R = \\sqrt{144 + 25} = \\sqrt{169} = 13\\)."
            },
            {
                "id": "ex16-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Evaluate: \\( \\frac{9 \\times 10^9 \\times (2 \\times 10^{-6})^2}{(0.3)^2} \\)",
                "answer": 0.4, "displayAnswer": "0.4", "tolerance": 0.01, "unit": "N",
                "hint": "9*10^9 * 4*10^-12 / 0.09 = 36*10^-3 / 0.09 = 36 / 90 = 0.4.",
                "explanation": "\\(\\frac{36 \\times 10^{-3}}{0.09} = 0.4 \\text{ N}\\)."
            },
            {
                "id": "ex16-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A force of \\( 50 \\text{ N} \\) acts at an angle \\( 60^\\circ \\) to the horizontal. Find its horizontal component \\( F_x = F \\cos 60^\\circ \\) in Newtons. (\\( \\cos 60^\\circ = 0.5 \\))",
                "answer": 25, "displayAnswer": "25", "tolerance": 0.01, "unit": "N",
                "hint": "50 * 0.5 = 25.",
                "explanation": "\\(F_x = 50 \\times 0.5 = 25 \\text{ N}\\)."
            }
        ]
    },
    {
        "id": 17,
        "title": "Intermediate → Advanced: Trigonometric Values (30°, 45°, 60°)",
        "subtitle": "Calculate resolved force components, work with angles, and projectile range components.",
        "difficulty": 4,
        "tier": "Intermediate → Advanced",
        "estimatedMinutes": 20,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex17-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 100 \\times \\sin 30^\\circ \\)",
                "answer": 50, "displayAnswer": "50", "tolerance": 0, "unit": "",
                "hint": "sin 30° = 0.5.",
                "explanation": "\\(100 \\times 0.5 = 50\\)."
            },
            {
                "id": "ex17-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 20\\sqrt{2} \\times \\cos 45^\\circ \\)",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.01, "unit": "",
                "hint": "cos 45° = 1 / sqrt(2).",
                "explanation": "\\(20\\sqrt{2} \\times \\frac{1}{\\sqrt{2}} = 20\\)."
            },
            {
                "id": "ex17-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 40 \\times \\sin 60^\\circ \\). (Use \\( \\sin 60^\\circ \\approx 0.866 \\))",
                "answer": 34.64, "displayAnswer": "34.64 (or 20√3)", "tolerance": 0.1, "unit": "",
                "hint": "40 * (sqrt(3)/2) = 20 * 1.732 = 34.64.",
                "explanation": "\\(20 \\times 1.732 = 34.64\\)."
            },
            {
                "id": "ex17-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\tan^2 60^\\circ - \\tan^2 45^\\circ \\)",
                "answer": 2, "displayAnswer": "2", "tolerance": 0, "unit": "",
                "hint": "tan 60° = sqrt(3) => tan^2 60° = 3. tan 45° = 1. 3 - 1 = 2.",
                "explanation": "\\(3 - 1 = 2\\)."
            },
            {
                "id": "ex17-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 2 \\sin 30^\\circ \\cos 30^\\circ \\times 10 \\). (Recall \\( \\sin 60^\\circ \\approx 0.866 \\))",
                "answer": 8.66, "displayAnswer": "8.66 (or 5√3)", "tolerance": 0.05, "unit": "",
                "hint": "2 sin 30 cos 30 = sin 60 = sqrt(3)/2. 10 * 0.866 = 8.66.",
                "explanation": "\\(10 \\times \\sin 60^\\circ = 10 \\times 0.866 = 8.66\\)."
            },
            # Algebra (5)
            {
                "id": "ex17-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\frac{x^2 - 16}{x + 4} = 6 \\)",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "",
                "hint": "x - 4 = 6 => x = 10.",
                "explanation": "\\(x - 4 = 6 \\implies x = 10\\)."
            },
            {
                "id": "ex17-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\sin\\theta = \\frac{1}{2} \\) where \\( 0^\\circ < \\theta < 90^\\circ \\), find \\( \\cos^2\\theta \\). Enter as decimal.",
                "answer": 0.75, "displayAnswer": "0.75 (or 3/4)", "tolerance": 0.01, "unit": "",
                "hint": "cos^2 theta = 1 - sin^2 theta = 1 - 0.25 = 0.75.",
                "explanation": "\\(1 - \\left(\\frac{1}{2}\\right)^2 = 1 - \\frac{1}{4} = 0.75\\)."
            },
            {
                "id": "ex17-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\sqrt{3} x - 6 = 0 \\). Express as decimal to 2 places.",
                "answer": 3.46, "displayAnswer": "3.46 (or 2√3)", "tolerance": 0.05, "unit": "",
                "hint": "x = 6 / sqrt(3) = 2*sqrt(3) ≈ 3.464.",
                "explanation": "\\(x = 2\\sqrt{3} \\approx 3.46\\)."
            },
            {
                "id": "ex17-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the larger root of \\( 2x^2 - 9x + 10 = 0 \\).",
                "answer": 2.5, "displayAnswer": "2.5 (roots are 2, 2.5)", "tolerance": 0.01, "unit": "",
                "hint": "(2x - 5)(x - 2) = 0.",
                "explanation": "Roots are 2 and 2.5. Larger root is 2.5."
            },
            {
                "id": "ex17-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Evaluate \\( \\frac{1}{\\sqrt{2}+1} \\) to 2 decimal places. (Rationalize denominator)",
                "answer": 0.41, "displayAnswer": "0.41 (√2 - 1)", "tolerance": 0.02, "unit": "",
                "hint": "(sqrt(2) - 1)/(2 - 1) = sqrt(2) - 1 = 1.414 - 1 = 0.414.",
                "explanation": "\\(\\sqrt{2} - 1 \\approx 0.414\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex17-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Work done is \\( W = F s \\cos\\theta \\). If \\( F = 40 \\text{ N} \\), \\( s = 5 \\text{ m} \\), and \\( \\theta = 60^\\circ \\), find \\( W \\) in Joules.",
                "answer": 100, "displayAnswer": "100", "tolerance": 0.01, "unit": "J",
                "hint": "W = 40 * 5 * 0.5 = 100 J.",
                "explanation": "\\(W = 40 \\times 5 \\times 0.5 = 100 \\text{ J}\\)."
            },
            {
                "id": "ex17-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A projectile is launched with velocity \\( u = 20 \\text{ m/s} \\) at angle \\( 30^\\circ \\) to horizontal. Calculate the vertical component of velocity \\( u_y = u \\sin 30^\\circ \\) in \\( \\text{m/s} \\).",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "m/s",
                "hint": "20 * 0.5 = 10.",
                "explanation": "\\(u_y = 20 \\times 0.5 = 10 \\text{ m/s}\\)."
            },
            {
                "id": "ex17-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "For the same projectile, maximum height is \\( H = \\frac{u_y^2}{2g} \\). With \\( u_y = 10 \\text{ m/s} \\) and \\( g = 10 \\text{ m/s}^2 \\), find \\( H \\) in meters.",
                "answer": 5, "displayAnswer": "5", "tolerance": 0.01, "unit": "m",
                "hint": "100 / 20 = 5.",
                "explanation": "\\(H = \\frac{100}{20} = 5 \\text{ m}\\)."
            },
            {
                "id": "ex17-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Centripetal acceleration is \\( a_c = \\frac{v^2}{r} \\). If \\( v = 15 \\text{ m/s} \\) and radius \\( r = 5 \\text{ m} \\), calculate \\( a_c \\) in \\( \\text{m/s}^2 \\).",
                "answer": 45, "displayAnswer": "45", "tolerance": 0.01, "unit": "m/s²",
                "hint": "15^2 / 5 = 225 / 5 = 45.",
                "explanation": "\\(a_c = \\frac{225}{5} = 45 \\text{ m/s}^2\\)."
            },
            {
                "id": "ex17-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Torque is \\( \\tau = F r \\sin\\theta \\). If \\( F = 20 \\text{ N} \\), arm length \\( r = 0.5 \\text{ m} \\), and \\( \\theta = 30^\\circ \\), find torque \\( \\tau \\) in \\( \\text{N}\\cdot\\text{m} \\).",
                "answer": 5, "displayAnswer": "5", "tolerance": 0.01, "unit": "N·m",
                "hint": "20 * 0.5 * 0.5 = 5.",
                "explanation": "\\(\\tau = 20 \\times 0.5 \\times 0.5 = 5 \\text{ N}\\cdot\\text{m}\\)."
            }
        ]
    },
    {
        "id": 18,
        "title": "Intermediate → Advanced: The 3-4-5 Triangle (37° & 53°)",
        "subtitle": "Master the universal NEET/JEE mechanics angles: sin 37° = 0.6, cos 37° = 0.8, tan 37° = 3/4.",
        "difficulty": 4,
        "tier": "Intermediate → Advanced",
        "estimatedMinutes": 20,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex18-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Using \\( \\sin 37^\\circ = 0.6 \\), calculate: \\( 50 \\times \\sin 37^\\circ \\)",
                "answer": 30, "displayAnswer": "30", "tolerance": 0, "unit": "",
                "hint": "50 * 0.6 = 30.",
                "explanation": "\\(50 \\times 0.6 = 30\\)."
            },
            {
                "id": "ex18-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Using \\( \\cos 37^\\circ = 0.8 \\), calculate: \\( 50 \\times \\cos 37^\\circ \\)",
                "answer": 40, "displayAnswer": "40", "tolerance": 0, "unit": "",
                "hint": "50 * 0.8 = 40.",
                "explanation": "\\(50 \\times 0.8 = 40\\)."
            },
            {
                "id": "ex18-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Recall \\( \\sin 53^\\circ = \\cos 37^\\circ = 0.8 \\). Calculate: \\( 25 \\times \\sin 53^\\circ \\)",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "",
                "hint": "25 * 0.8 = 20.",
                "explanation": "\\(25 \\times 0.8 = 20\\)."
            },
            {
                "id": "ex18-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\tan 37^\\circ \\times 80 \\). (Recall \\( \\tan 37^\\circ = 3/4 = 0.75 \\))",
                "answer": 60, "displayAnswer": "60", "tolerance": 0, "unit": "",
                "hint": "(3/4) * 80 = 3 * 20 = 60.",
                "explanation": "\\(0.75 \\times 80 = 60\\)."
            },
            {
                "id": "ex18-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\sqrt{30^2 + 40^2} \\)",
                "answer": 50, "displayAnswer": "50", "tolerance": 0, "unit": "",
                "hint": "10 * sqrt(3^2 + 4^2) = 10 * 5 = 50.",
                "explanation": "\\(\\sqrt{900 + 1600} = \\sqrt{2500} = 50\\)."
            },
            # Algebra (5)
            {
                "id": "ex18-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\tan\\theta = \\frac{3}{4} \\), what is the value of \\( 5\\sin\\theta + 5\\cos\\theta \\)?",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "sin theta = 3/5, cos theta = 4/5. 5*(3/5 + 4/5) = 3 + 4 = 7.",
                "explanation": "\\(3 + 4 = 7\\)."
            },
            {
                "id": "ex18-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( 0.8 x - 0.6(x + 5) = 3 \\)",
                "answer": 30, "displayAnswer": "30", "tolerance": 0, "unit": "",
                "hint": "0.8x - 0.6x - 3 = 3 => 0.2x = 6 => x = 30.",
                "explanation": "\\(0.2x = 6 \\implies x = 30\\)."
            },
            {
                "id": "ex18-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the smaller positive root of \\( 4x^2 - 12x + 5 = 0 \\).",
                "answer": 0.5, "displayAnswer": "0.5 (roots are 0.5, 2.5)", "tolerance": 0.01, "unit": "",
                "hint": "(2x - 1)(2x - 5) = 0 => x = 1/2, 5/2.",
                "explanation": "Roots are 0.5 and 2.5. Smaller root is 0.5."
            },
            {
                "id": "ex18-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\vec{A} = 3\\hat{i} + 4\\hat{j} \\) and \\( \\vec{B} = 4\\hat{i} - 3\\hat{j} \\), find the dot product \\( \\vec{A} \\cdot \\vec{B} \\).",
                "answer": 0, "displayAnswer": "0", "tolerance": 0, "unit": "",
                "hint": "3*4 + 4*(-3) = 12 - 12 = 0. They are perpendicular!",
                "explanation": "\\(3(4) + 4(-3) = 12 - 12 = 0\\)."
            },
            {
                "id": "ex18-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( \\frac{x^2 - 25}{x - 5} = 12 \\)",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "x + 5 = 12 => x = 7.",
                "explanation": "\\(x + 5 = 12 \\implies x = 7\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex18-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A block of mass \\( m = 10 \\text{ kg} \\) rests on an incline of angle \\( \\theta = 37^\\circ \\). Calculate the component of gravity down the incline \\( F_{\\parallel} = mg \\sin 37^\\circ \\) in Newtons. (Take \\( g = 10 \\text{ m/s}^2 \\), \\( \\sin 37^\\circ = 0.6 \\))",
                "answer": 60, "displayAnswer": "60", "tolerance": 0.01, "unit": "N",
                "hint": "10 * 10 * 0.6 = 60.",
                "explanation": "\\(F_{\\parallel} = 10 \\times 10 \\times 0.6 = 60 \\text{ N}\\)."
            },
            {
                "id": "ex18-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "For the same block, calculate normal force \\( N = mg \\cos 37^\\circ \\) in Newtons. (\\( \\cos 37^\\circ = 0.8 \\))",
                "answer": 80, "displayAnswer": "80", "tolerance": 0.01, "unit": "N",
                "hint": "10 * 10 * 0.8 = 80.",
                "explanation": "\\(N = 10 \\times 10 \\times 0.8 = 80 \\text{ N}\\)."
            },
            {
                "id": "ex18-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "If coefficient of friction is \\( \\mu = 0.5 \\), calculate maximum static friction \\( f_{\\text{max}} = \\mu N \\) in Newtons. (With \\( N = 80 \\text{ N} \\))",
                "answer": 40, "displayAnswer": "40", "tolerance": 0.01, "unit": "N",
                "hint": "0.5 * 80 = 40.",
                "explanation": "\\(f_{\\text{max}} = 0.5 \\times 80 = 40 \\text{ N}\\)."
            },
            {
                "id": "ex18-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A projectile is launched with velocity \\( 50 \\text{ m/s} \\) at angle \\( 53^\\circ \\) above horizontal. What is its horizontal velocity component \\( u_x = u \\cos 53^\\circ \\) in \\( \\text{m/s} \\)? (\\( \\cos 53^\\circ = 0.6 \\))",
                "answer": 30, "displayAnswer": "30", "tolerance": 0.01, "unit": "m/s",
                "hint": "50 * 0.6 = 30.",
                "explanation": "\\(u_x = 50 \\times 0.6 = 30 \\text{ m/s}\\)."
            },
            {
                "id": "ex18-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the initial vertical velocity component \\( u_y = u \\sin 53^\\circ \\) in \\( \\text{m/s} \\) for the same projectile? (\\( \\sin 53^\\circ = 0.8 \\))",
                "answer": 40, "displayAnswer": "40", "tolerance": 0.01, "unit": "m/s",
                "hint": "50 * 0.8 = 40.",
                "explanation": "\\(u_y = 50 \\times 0.8 = 40 \\text{ m/s}\\)."
            }
        ]
    },
    {
        "id": 19,
        "title": "Intermediate → Advanced: Vector Resultants & Dot Products",
        "subtitle": "Calculate vector addition with angles, work as scalar product W = F·s, and power as P = F·v.",
        "difficulty": 4,
        "tier": "Intermediate → Advanced",
        "estimatedMinutes": 20,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex19-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Resultant of two equal forces \\( F \\) at \\( 60^\\circ \\) is \\( R = 2F\\cos(30^\\circ) = \\sqrt{3}F \\). If \\( F = 10 \\text{ N} \\), evaluate \\( R \\) to 2 decimal places.",
                "answer": 17.32, "displayAnswer": "17.32 (or 10√3)", "tolerance": 0.05, "unit": "N",
                "hint": "10 * 1.732 = 17.32.",
                "explanation": "\\(10 \\times \\sqrt{3} \\approx 17.32 \\text{ N}\\)."
            },
            {
                "id": "ex19-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Two equal forces of \\( 20 \\text{ N} \\) act at an angle of \\( 120^\\circ \\). What is their resultant magnitude? (Recall: \\( R = F \\) when angle is \\( 120^\\circ \\))",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "N",
                "hint": "R = 2*20*cos(60°) = 2*20*0.5 = 20.",
                "explanation": "\\(R = 2F\\cos(60^\\circ) = 20 \\text{ N}\\)."
            },
            {
                "id": "ex19-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( 15^2 + 20^2 \\)",
                "answer": 625, "displayAnswer": "625", "tolerance": 0, "unit": "",
                "hint": "225 + 400 = 625 = 25^2.",
                "explanation": "\\(225 + 400 = 625\\)."
            },
            {
                "id": "ex19-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\frac{1.5 \\times 10^8}{3 \\times 10^5} \\)",
                "answer": 500, "displayAnswer": "500", "tolerance": 0.1, "unit": "",
                "hint": "0.5 * 10^3 = 500.",
                "explanation": "\\(0.5 \\times 10^3 = 500\\)."
            },
            {
                "id": "ex19-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 18 \\times 2.5 \\times 4 \\)",
                "answer": 180, "displayAnswer": "180", "tolerance": 0, "unit": "",
                "hint": "2.5 * 4 = 10. 18 * 10 = 180.",
                "explanation": "\\(18 \\times 10 = 180\\)."
            },
            # Algebra (5)
            {
                "id": "ex19-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( \\vec{F} = 6\\hat{i} + 8\\hat{j} \\text{ N} \\) and displacement \\( \\vec{s} = 3\\hat{i} + 2\\hat{j} \\text{ m} \\), calculate work done \\( W = \\vec{F} \\cdot \\vec{s} \\) in Joules.",
                "answer": 34, "displayAnswer": "34", "tolerance": 0, "unit": "J",
                "hint": "6*3 + 8*2 = 18 + 16 = 34.",
                "explanation": "\\(W = 6(3) + 8(2) = 18 + 16 = 34 \\text{ J}\\)."
            },
            {
                "id": "ex19-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the magnitude of vector \\( \\vec{A} = 2\\hat{i} + 3\\hat{j} + 6\\hat{k} \\): \\( |\\vec{A}| = \\sqrt{2^2 + 3^2 + 6^2} \\).",
                "answer": 7, "displayAnswer": "7", "tolerance": 0, "unit": "",
                "hint": "sqrt(4 + 9 + 36) = sqrt(49) = 7.",
                "explanation": "\\(\\sqrt{4 + 9 + 36} = \\sqrt{49} = 7\\)."
            },
            {
                "id": "ex19-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{5}{x-2} = \\frac{7}{x+4} \\)",
                "answer": 17, "displayAnswer": "17", "tolerance": 0, "unit": "",
                "hint": "5(x + 4) = 7(x - 2) => 5x + 20 = 7x - 14 => 2x = 34.",
                "explanation": "\\(2x = 34 \\implies x = 17\\)."
            },
            {
                "id": "ex19-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Find the roots of \\( 6x^2 - 7x + 2 = 0 \\). Enter the larger root as decimal.",
                "answer": 0.67, "displayAnswer": "0.67 (or 2/3)", "tolerance": 0.02, "unit": "",
                "hint": "(2x - 1)(3x - 2) = 0 => x = 1/2 = 0.5, x = 2/3 ≈ 0.667.",
                "explanation": "Larger root is 2/3 ≈ 0.667."
            },
            {
                "id": "ex19-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If angle between vectors \\( \\vec{A} \\) and \\( \\vec{B} \\) is \\( 90^\\circ \\) and \\( \\vec{A} = 2\\hat{i} + c\\hat{j} \\), \\( \\vec{B} = 6\\hat{i} - 4\\hat{j} \\), find \\( c \\).",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "2*6 + c*(-4) = 0 => 12 - 4c = 0 => c = 3.",
                "explanation": "\\(12 - 4c = 0 \\implies c = 3\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex19-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A motor delivers a force \\( \\vec{F} = (20\\hat{i} + 15\\hat{j}) \\text{ N} \\) to a vehicle moving at constant velocity \\( \\vec{v} = (3\\hat{i} + 2\\hat{j}) \\text{ m/s} \\). Calculate power \\( P = \\vec{F} \\cdot \\vec{v} \\) in Watts.",
                "answer": 90, "displayAnswer": "90", "tolerance": 0.01, "unit": "W",
                "hint": "20*3 + 15*2 = 60 + 30 = 90 W.",
                "explanation": "\\(P = 60 + 30 = 90 \\text{ W}\\)."
            },
            {
                "id": "ex19-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Two forces \\( F_1 = 8 \\text{ N} \\) and \\( F_2 = 6 \\text{ N} \\) act at right angles (\\( 90^\\circ \\)). Calculate the magnitude of the resultant force in Newtons.",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "N",
                "hint": "sqrt(64 + 36) = sqrt(100) = 10.",
                "explanation": "\\(R = \\sqrt{64 + 36} = 10 \\text{ N}\\)."
            },
            {
                "id": "ex19-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Escape velocity from Earth is \\( v_e = \\sqrt{2gR} \\). If \\( g = 9.8 \\text{ m/s}^2 \\) and \\( R = 6.4 \\times 10^6 \\text{ m} \\), calculate \\( v_e \\) in \\( \\text{km/s} \\) to 1 decimal place. (\\( \\sqrt{125.44} = 11.2 \\))",
                "answer": 11.2, "displayAnswer": "11.2", "tolerance": 0.1, "unit": "km/s",
                "hint": "sqrt(2 * 9.8 * 6.4 * 10^6) = sqrt(125.44 * 10^6) = 11.2 * 10^3 m/s = 11.2 km/s.",
                "explanation": "\\(v_e = 11.2 \\text{ km/s}\\)."
            },
            {
                "id": "ex19-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A sphere has radius \\( r = 2 \\text{ cm} \\). What is its surface area in \\( \\text{cm}^2 \\)? Express in terms of \\( \\pi \\): if Area \\( = k\\pi \\), what is \\( k \\)? (\\( A = 4\\pi r^2 \\))",
                "answer": 16, "displayAnswer": "16 (Area is 16π cm²)", "tolerance": 0, "unit": "",
                "hint": "4 * r^2 = 4 * 4 = 16.",
                "explanation": "\\(4 \\times 2^2 = 16\\)."
            },
            {
                "id": "ex19-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A current of \\( 4 \\text{ A} \\) flows through an inductor of inductance \\( L = 0.5 \\text{ H} \\). Calculate stored magnetic energy \\( U = \\frac{1}{2}LI^2 \\) in Joules.",
                "answer": 4, "displayAnswer": "4", "tolerance": 0.01, "unit": "J",
                "hint": "0.5 * 0.5 * 16 = 0.25 * 16 = 4 J.",
                "explanation": "\\(U = 0.5 \\times 0.5 \\times 16 = 4 \\text{ J}\\)."
            }
        ]
    },
    {
        "id": 20,
        "title": "Intermediate → Advanced: Universal Gravitation & Inverse Square Law",
        "subtitle": "Calculate inverse-square scaling, orbital speed, and Coulomb electrostatic forces.",
        "difficulty": 4,
        "tier": "Intermediate → Advanced",
        "estimatedMinutes": 20,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex20-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "If distance \\( r \\) between two masses is tripled (\\( 3r \\)), by what factor does the gravitational force change? Enter as decimal.",
                "answer": 0.111, "displayAnswer": "0.111 (or 1/9)", "tolerance": 0.01, "unit": "",
                "hint": "Inverse square: 1 / 3^2 = 1/9 ≈ 0.111.",
                "explanation": "\\(1 / 3^2 = 1/9 \\approx 0.111\\)."
            },
            {
                "id": "ex20-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "If distance \\( r \\) is halved (\\( r/2 \\)), by what factor does the force increase?",
                "answer": 4, "displayAnswer": "4", "tolerance": 0, "unit": "",
                "hint": "1 / (1/2)^2 = 4.",
                "explanation": "\\(1 / (1/2)^2 = 4\\)."
            },
            {
                "id": "ex20-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{6.67 \\times 10^{-11} \\times 6 \\times 10^{24}}{(6.4 \\times 10^6)^2} \\). What is this approximate surface gravity value in \\( \\text{m/s}^2 \\)?",
                "answer": 9.8, "displayAnswer": "9.8", "tolerance": 0.2, "unit": "m/s²",
                "hint": "This is g at Earth's surface: ~9.8 m/s^2.",
                "explanation": "\\(g \\approx 9.77 \\approx 9.8 \\text{ m/s}^2\\)."
            },
            {
                "id": "ex20-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\sqrt{1.96 \\times 10^6} \\)",
                "answer": 1400, "displayAnswer": "1400", "tolerance": 1, "unit": "",
                "hint": "sqrt(1.96) * 10^3 = 1.4 * 1000 = 1400.",
                "explanation": "\\(1.4 \\times 1000 = 1400\\)."
            },
            {
                "id": "ex20-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 225 \\times 0.04 \\)",
                "answer": 9, "displayAnswer": "9", "tolerance": 0.01, "unit": "",
                "hint": "225 / 25 = 9.",
                "explanation": "\\(225 \\times 0.04 = 9\\)."
            },
            # Algebra (5)
            {
                "id": "ex20-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( r \\): \\( \\frac{k}{r^2} = 400 \\), given \\( k = 3600 \\).",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "r^2 = 3600 / 400 = 9 => r = 3.",
                "explanation": "\\(r^2 = 9 \\implies r = 3\\)."
            },
            {
                "id": "ex20-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If \\( g' = g\\left(1 - \\frac{2h}{R}\\right) \\), and \\( \\frac{h}{R} = 0.01 \\), find \\( \\frac{g'}{g} \\). Enter as decimal.",
                "answer": 0.98, "displayAnswer": "0.98", "tolerance": 0.005, "unit": "",
                "hint": "1 - 2(0.01) = 1 - 0.02 = 0.98.",
                "explanation": "\\(1 - 0.02 = 0.98\\)."
            },
            {
                "id": "ex20-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for \\( x \\): \\( \\frac{x^2 - 49}{x - 7} = 20 \\)",
                "answer": 13, "displayAnswer": "13", "tolerance": 0, "unit": "",
                "hint": "x + 7 = 20 => x = 13.",
                "explanation": "\\(x + 7 = 20 \\implies x = 13\\)."
            },
            {
                "id": "ex20-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If Kepler's law states \\( T^2 \\propto R^3 \\), and \\( R \\) is increased by a factor of 4, by what factor does period \\( T \\) increase?",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "T increases by 4^(3/2) = (sqrt(4))^3 = 2^3 = 8.",
                "explanation": "\\(4^{3/2} = 2^3 = 8\\)."
            },
            {
                "id": "ex20-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Solve for positive \\( x \\): \\( 2x^2 - 18 = 0 \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "x^2 = 9 => x = 3.",
                "explanation": "\\(x = 3\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex20-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Weight of a body on Earth is \\( 180 \\text{ N} \\). At a height \\( h = R \\) (distance \\( 2R \\) from center), what is its weight in Newtons? (\\( W' = W / (1 + h/R)^2 \\))",
                "answer": 45, "displayAnswer": "45", "tolerance": 0.01, "unit": "N",
                "hint": "180 / 2^2 = 180 / 4 = 45.",
                "explanation": "\\(W' = \\frac{180}{4} = 45 \\text{ N}\\)."
            },
            {
                "id": "ex20-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Orbital speed near Earth surface is \\( v_0 = \\sqrt{gR} \\). If \\( g = 10 \\text{ m/s}^2 \\) and \\( R = 6.4 \\times 10^6 \\text{ m} \\), find \\( v_0 \\) in \\( \\text{km/s} \\).",
                "answer": 8, "displayAnswer": "8", "tolerance": 0.1, "unit": "km/s",
                "hint": "sqrt(64 * 10^6) = 8 * 10^3 m/s = 8 km/s.",
                "explanation": "\\(v_0 = 8000 \\text{ m/s} = 8 \\text{ km/s}\\)."
            },
            {
                "id": "ex20-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate the electric field \\( E = \\frac{kq}{r^2} \\). If \\( k = 9 \\times 10^9 \\text{ N}\\cdot\\text{m}^2/\\text{C}^2 \\), \\( q = 4 \\times 10^{-9} \\text{ C} \\), and \\( r = 0.2 \\text{ m} \\), find \\( E \\) in \\( \\text{N/C} \\).",
                "answer": 900, "displayAnswer": "900", "tolerance": 1, "unit": "N/C",
                "hint": "9*10^9 * 4*10^-9 / 0.04 = 36 / 0.04 = 900.",
                "explanation": "\\(E = \\frac{36}{0.04} = 900 \\text{ N/C}\\)."
            },
            {
                "id": "ex20-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A capacitor stores energy \\( U = \\frac{1}{2}CV^2 \\). If \\( C = 400 \\text{ }\\mu\\text{F} \\) and \\( V = 50 \\text{ V} \\), calculate stored energy \\( U \\) in Joules.",
                "answer": 0.5, "displayAnswer": "0.5", "tolerance": 0.01, "unit": "J",
                "hint": "0.5 * (400 * 10^-6) * 2500 = 0.5 * 1 = 0.5 J.",
                "explanation": "\\(U = 0.5 \\times 400 \\times 10^{-6} \\times 2500 = 0.5 \\text{ J}\\)."
            },
            {
                "id": "ex20-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A wire of resistance \\( 12 \\text{ }\\Omega \\) is stretched to double its original length (volume constant). What is its new resistance in \\( \\Omega \\)? (Recall: \\( R' = n^2 R \\))",
                "answer": 48, "displayAnswer": "48", "tolerance": 0, "unit": "Ω",
                "hint": "R' = 2^2 * 12 = 4 * 12 = 48.",
                "explanation": "\\(R' = 4 \\times 12 = 48 \\text{ }\\Omega\\)."
            }
        ]
    }
]

print(f"Tier 4 loaded: {len(tier4)} exercises.")
