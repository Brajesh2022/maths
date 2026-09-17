# Tier 6: Exercises 26 - 30 (Exam-Level NEET/JEE Numericals)

tier6 = [
    {
        "id": 26,
        "title": "Exam-Level: Bohr Model & Atomic Spectra",
        "subtitle": "Calculate energy levels En = -13.6/n² eV, orbital radii, and Lyman/Balmer transition wavelengths.",
        "difficulty": 5,
        "tier": "Exam-Level",
        "estimatedMinutes": 25,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex26-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Using Bohr formula \\( E_n = -\\frac{13.6}{n^2} \\text{ eV} \\), calculate ground state energy \\( E_1 \\) in eV.",
                "answer": -13.6, "displayAnswer": "-13.6", "tolerance": 0.05, "unit": "eV",
                "hint": "n = 1 => -13.6 / 1 = -13.6 eV.",
                "explanation": "\\(E_1 = -13.6 \\text{ eV}\\)."
            },
            {
                "id": "ex26-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate energy of first excited state \\( E_2 \\) (\\( n = 2 \\)) in eV.",
                "answer": -3.4, "displayAnswer": "-3.4", "tolerance": 0.05, "unit": "eV",
                "hint": "-13.6 / 4 = -3.4 eV.",
                "explanation": "\\(E_2 = -\\frac{13.6}{4} = -3.4 \\text{ eV}\\)."
            },
            {
                "id": "ex26-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate excitation energy to promote electron from \\( n = 1 \\) to \\( n = 2 \\): \\( \\Delta E = E_2 - E_1 \\) in eV.",
                "answer": 10.2, "displayAnswer": "10.2", "tolerance": 0.05, "unit": "eV",
                "hint": "-3.4 - (-13.6) = 13.6 - 3.4 = 10.2 eV.",
                "explanation": "\\(\\Delta E = 10.2 \\text{ eV}\\). Standard Lyman-alpha value!"
            },
            {
                "id": "ex26-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate energy of third orbit \\( E_3 \\) (\\( n = 3 \\)) in eV to 2 decimal places.",
                "answer": -1.51, "displayAnswer": "-1.51", "tolerance": 0.03, "unit": "eV",
                "hint": "-13.6 / 9 ≈ -1.511 eV.",
                "explanation": "\\(E_3 = -\\frac{13.6}{9} \\approx -1.51 \\text{ eV}\\)."
            },
            {
                "id": "ex26-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate energy of fourth orbit \\( E_4 \\) (\\( n = 4 \\)) in eV.",
                "answer": -0.85, "displayAnswer": "-0.85", "tolerance": 0.02, "unit": "eV",
                "hint": "-13.6 / 16 = -0.85 eV.",
                "explanation": "\\(E_4 = -\\frac{13.6}{16} = -0.85 \\text{ eV}\\)."
            },
            # Algebra (5)
            {
                "id": "ex26-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Using \\( \\lambda = \\frac{1240}{\\Delta E \\text{ (in eV)}} \\text{ nm} \\), calculate wavelength of Lyman-alpha line (\\( \\Delta E = 10.2 \\text{ eV} \\)) in nm to nearest integer.",
                "answer": 121.5, "displayAnswer": "121.5 (approx 122 nm)", "tolerance": 2, "unit": "nm",
                "hint": "1240 / 10.2 ≈ 121.57 nm.",
                "explanation": "\\(\\lambda = \\frac{1240}{10.2} \\approx 121.6 \\text{ nm}\\)."
            },
            {
                "id": "ex26-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Bohr radius is \\( r_n = 0.529 n^2 \\text{ \\AA} \\). Calculate the radius of the second orbit (\\( n = 2 \\)) in Angstroms.",
                "answer": 2.116, "displayAnswer": "2.116 (or 2.12 Å)", "tolerance": 0.05, "unit": "Å",
                "hint": "0.529 * 4 = 2.116 Å.",
                "explanation": "\\(r_2 = 0.529 \\times 4 = 2.116 \\text{ \\AA}\\)."
            },
            {
                "id": "ex26-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "In Balmer series, electron jumps from \\( n = 3 \\) to \\( n = 2 \\). Energy released is \\( E_3 - E_2 = -1.51 - (-3.40) \\). Calculate \\( \\Delta E \\) in eV.",
                "answer": 1.89, "displayAnswer": "1.89", "tolerance": 0.03, "unit": "eV",
                "hint": "3.40 - 1.51 = 1.89 eV.",
                "explanation": "\\(\\Delta E = 3.40 - 1.51 = 1.89 \\text{ eV}\\)."
            },
            {
                "id": "ex26-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Calculate the wavelength of this red \\( H_\\alpha \\) line: \\( \\lambda = \\frac{1240}{1.89 \\text{ eV}} \\) in nm to nearest whole number.",
                "answer": 656, "displayAnswer": "656", "tolerance": 5, "unit": "nm",
                "hint": "1240 / 1.89 ≈ 656 nm (famous H-alpha wavelength!).",
                "explanation": "\\(\\lambda \\approx 656 \\text{ nm}\\)."
            },
            {
                "id": "ex26-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "What is the ratio of orbital frequencies \\( f_1 / f_2 \\) in Bohr model? (Recall \\( f \\propto \\frac{1}{n^3} \\))",
                "answer": 8, "displayAnswer": "8", "tolerance": 0, "unit": "",
                "hint": "(2 / 1)^3 = 8.",
                "explanation": "\\(\\frac{f_1}{f_2} = \\left(\\frac{2}{1}\\right)^3 = 8\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex26-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Rydberg constant \\( R \\approx 1.097 \\times 10^7 \\text{ m}^{-1} \\). What is \\( \\frac{1}{R} \\) in nanometers? (Famous shortcut: \\( 1/R \\approx 91.2 \\text{ nm} \\))",
                "answer": 91.2, "displayAnswer": "91.2", "tolerance": 0.5, "unit": "nm",
                "hint": "1 / (1.097 * 10^7) = 9.115 * 10^-8 m ≈ 91.2 nm.",
                "explanation": "\\(\\frac{1}{R} \\approx 91.2 \\text{ nm}\\). Memorize 1/R = 912 Å for instant NEET/JEE spectra solving!"
            },
            {
                "id": "ex26-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Shortest wavelength of Lyman series (series limit, \\( n = \\infty \\to 1 \\)) is \\( \\lambda_{\\text{min}} = \\frac{1}{R} \\). In nm, this is approximately:",
                "answer": 91.2, "displayAnswer": "91.2", "tolerance": 0.5, "unit": "nm",
                "hint": "91.2 nm.",
                "explanation": "\\(\\lambda_{\\text{min}} = 91.2 \\text{ nm}\\)."
            },
            {
                "id": "ex26-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Shortest wavelength of Balmer series (series limit, \\( n = \\infty \\to 2 \\)) is \\( \\frac{4}{R} = 4 \\times 91.2 \\text{ nm} \\). Calculate this value in nm.",
                "answer": 364.8, "displayAnswer": "364.8", "tolerance": 1, "unit": "nm",
                "hint": "4 * 91.2 = 364.8 nm.",
                "explanation": "\\(4 \\times 91.2 = 364.8 \\text{ nm}\\)."
            },
            {
                "id": "ex26-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Ionization potential of \\( \\text{He}^+ \\) ion (\\( Z = 2 \\)) from ground state is \\( 13.6 \\times Z^2 \\text{ eV} \\). Calculate this value in eV.",
                "answer": 54.4, "displayAnswer": "54.4", "tolerance": 0.1, "unit": "eV",
                "hint": "13.6 * 4 = 54.4 eV.",
                "explanation": "\\(13.6 \\times 4 = 54.4 \\text{ eV}\\)."
            },
            {
                "id": "ex26-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Speed of electron in first Bohr orbit is \\( v_1 = \\frac{c}{137} \\). If speed of light \\( c = 3 \\times 10^8 \\text{ m/s} \\), calculate \\( v_1 \\times 10^{-6} \\text{ m/s} \\) to 2 decimal places.",
                "answer": 2.19, "displayAnswer": "2.19 (v₁ ≈ 2.19×10⁶ m/s)", "tolerance": 0.05, "unit": "",
                "hint": "300 / 137 ≈ 2.189 ≈ 2.19.",
                "explanation": "\\(v_1 = \\frac{3 \\times 10^8}{137} \\approx 2.19 \\times 10^6 \\text{ m/s}\\)."
            }
        ]
    },
    {
        "id": 27,
        "title": "Exam-Level: Ray Optics & Lens Formulae",
        "subtitle": "Master 1/f = 1/v - 1/u, lens maker formula, critical angle, and prism deviations.",
        "difficulty": 5,
        "tier": "Exam-Level",
        "estimatedMinutes": 25,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex27-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{20} - \\frac{1}{30} \\). Enter the reciprocal of this result (i.e. \\( x \\) if \\( \\frac{1}{x} = \\frac{1}{20} - \\frac{1}{30} \\)).",
                "answer": 60, "displayAnswer": "60", "tolerance": 0, "unit": "",
                "hint": "(3 - 2)/60 = 1/60 => reciprocal is 60.",
                "explanation": "\\(\\frac{1}{20} - \\frac{1}{30} = \\frac{1}{60}\\). Reciprocal is 60."
            },
            {
                "id": "ex27-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{15} + \\frac{1}{30} \\). Enter the reciprocal of this result.",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "",
                "hint": "(2 + 1)/30 = 3/30 = 1/10 => reciprocal is 10.",
                "explanation": "\\(\\frac{1}{15} + \\frac{1}{30} = \\frac{1}{10}\\). Reciprocal is 10."
            },
            {
                "id": "ex27-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate critical angle \\( C \\) in degrees for glass-air interface if refractive index \\( \\mu = 2 \\). (\\( \\sin C = \\frac{1}{\\mu} = 0.5 \\))",
                "answer": 30, "displayAnswer": "30°", "tolerance": 0, "unit": "°",
                "hint": "sin(30°) = 0.5.",
                "explanation": "\\(\\sin C = 0.5 \\implies C = 30^\\circ\\)."
            },
            {
                "id": "ex27-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "For a thin prism with apex angle \\( A = 6^\\circ \\) and \\( \\mu = 1.5 \\), calculate angle of deviation \\( \\delta = (\\mu - 1)A \\) in degrees.",
                "answer": 3, "displayAnswer": "3°", "tolerance": 0, "unit": "°",
                "hint": "(1.5 - 1) * 6 = 0.5 * 6 = 3°.",
                "explanation": "\\(\\delta = 0.5 \\times 6^\\circ = 3^\\circ\\)."
            },
            {
                "id": "ex27-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Apparent depth of a pool is \\( d' = \\frac{d}{\\mu} \\). If real depth \\( d = 4 \\text{ m} \\) and \\( \\mu_{\\text{water}} = 4/3 \\), calculate apparent depth \\( d' \\) in meters.",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "m",
                "hint": "4 / (4/3) = 3 m.",
                "explanation": "\\(d' = 4 \\times \\frac{3}{4} = 3 \\text{ m}\\)."
            },
            # Algebra (5)
            {
                "id": "ex27-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Using convex lens formula \\( \\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u} \\), if focal length \\( f = +15 \\text{ cm} \\) and object distance \\( u = -30 \\text{ cm} \\), find image distance \\( v \\) in cm.",
                "answer": 30, "displayAnswer": "30", "tolerance": 0.1, "unit": "cm",
                "hint": "1/v = 1/f + 1/u = 1/15 - 1/30 = 1/30 => v = 30 cm.",
                "explanation": "\\(\\frac{1}{v} = \\frac{1}{15} - \\frac{1}{30} = \\frac{1}{30} \\implies v = 30 \\text{ cm}\\)."
            },
            {
                "id": "ex27-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "What is the linear magnification \\( m = \\frac{v}{u} \\) for this configuration (\\( v = +30 \\text{ cm}, u = -30 \\text{ cm} \\))?",
                "answer": -1, "displayAnswer": "-1", "tolerance": 0, "unit": "",
                "hint": "30 / (-30) = -1. Real, inverted, same size.",
                "explanation": "\\(m = \\frac{30}{-30} = -1\\)."
            },
            {
                "id": "ex27-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Now consider \\( u = -20 \\text{ cm} \\) for the same lens (\\( f = +15 \\text{ cm} \\)). Find \\( v \\) in cm. (\\( \\frac{1}{v} = \\frac{1}{15} - \\frac{1}{20} \\))",
                "answer": 60, "displayAnswer": "60", "tolerance": 0.1, "unit": "cm",
                "hint": "(4 - 3)/60 = 1/60 => v = 60 cm.",
                "explanation": "\\(\\frac{1}{v} = \\frac{1}{60} \\implies v = 60 \\text{ cm}\\)."
            },
            {
                "id": "ex27-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Calculate magnification \\( m = \\frac{v}{u} \\) for \\( v = +60 \\text{ cm}, u = -20 \\text{ cm} \\).",
                "answer": -3, "displayAnswer": "-3", "tolerance": 0, "unit": "",
                "hint": "60 / (-20) = -3.",
                "explanation": "\\(m = -3\\)."
            },
            {
                "id": "ex27-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Lens maker formula for equiconvex lens: \\( \\frac{1}{f} = (\\mu - 1)\\left(\\frac{2}{R}\\right) \\). If \\( \\mu = 1.5 \\) and radius of curvature \\( R = 20 \\text{ cm} \\), find focal length \\( f \\) in cm.",
                "answer": 20, "displayAnswer": "20", "tolerance": 0.1, "unit": "cm",
                "hint": "1/f = 0.5 * (2/20) = 1/20 => f = 20 cm.",
                "explanation": "\\(f = 20 \\text{ cm}\\). For glass (μ = 1.5) equiconvex lens, f = R!"
            },
            # Physics Calculations (5)
            {
                "id": "ex27-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "If this lens is submerged in water (\\( \\mu_w = 4/3 \\)), its new focal length is \\( f' = 4f \\). For \\( f = 20 \\text{ cm} \\), calculate \\( f' \\) in cm.",
                "answer": 80, "displayAnswer": "80", "tolerance": 0, "unit": "cm",
                "hint": "4 * 20 = 80 cm.",
                "explanation": "\\(f' = 4 \\times 20 = 80 \\text{ cm}\\). Focal length in water is 4 times that in air!"
            },
            {
                "id": "ex27-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Compound microscope magnification at normal adjustment is \\( M = \\left(\\frac{L}{f_o}\\right)\\left(\\frac{D}{f_e}\\right) \\). If tube length \\( L = 20 \\text{ cm} \\), \\( f_o = 1 \\text{ cm} \\), least distance \\( D = 25 \\text{ cm} \\), and \\( f_e = 5 \\text{ cm} \\), calculate \\( M \\).",
                "answer": 100, "displayAnswer": "100", "tolerance": 1, "unit": "",
                "hint": "(20 / 1) * (25 / 5) = 20 * 5 = 100.",
                "explanation": "\\(M = 20 \\times 5 = 100\\)."
            },
            {
                "id": "ex27-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Astronomical telescope has objective focal length \\( f_o = 100 \\text{ cm} \\) and eyepiece \\( f_e = 5 \\text{ cm} \\). Calculate its magnifying power \\( m = \\frac{f_o}{f_e} \\) in normal adjustment.",
                "answer": 20, "displayAnswer": "20", "tolerance": 0, "unit": "",
                "hint": "100 / 5 = 20.",
                "explanation": "\\(m = \\frac{100}{5} = 20\\)."
            },
            {
                "id": "ex27-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the tube length \\( L = f_o + f_e \\) in cm of this telescope?",
                "answer": 105, "displayAnswer": "105", "tolerance": 0, "unit": "cm",
                "hint": "100 + 5 = 105 cm.",
                "explanation": "\\(L = 100 + 5 = 105 \\text{ cm}\\)."
            },
            {
                "id": "ex27-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "In Young's Double Slit Experiment, fringe width is \\( \\beta = \\frac{\\lambda D}{d} \\). If wavelength \\( \\lambda = 6 \\times 10^{-7} \\text{ m} \\), slit separation \\( d = 1 \\text{ mm} = 10^{-3} \\text{ m} \\), and screen distance \\( D = 1 \\text{ m} \\), find \\( \\beta \\) in mm.",
                "answer": 0.6, "displayAnswer": "0.6", "tolerance": 0.01, "unit": "mm",
                "hint": "(6*10^-7 * 1) / 10^-3 = 6*10^-4 m = 0.6 mm.",
                "explanation": "\\(\\beta = 0.6 \\text{ mm}\\)."
            }
        ]
    },
    {
        "id": 28,
        "title": "Exam-Level: Electromagnetism & Cyclotron Motion",
        "subtitle": "Calculate magnetic field B = μ₀I/2πr, cyclotron radius r = mv/qB, and magnetic dipole moments.",
        "difficulty": 5,
        "tier": "Exam-Level",
        "estimatedMinutes": 25,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex28-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\frac{4\\pi \\times 10^{-7} \\times 10}{2\\pi \\times 0.1} \\). What is \\( B \\times 10^5 \\text{ T} \\)?",
                "answer": 2, "displayAnswer": "2 (B = 2×10⁻⁵ T)", "tolerance": 0.01, "unit": "",
                "hint": "(2 * 10^-7 * 10) / 0.1 = 20 * 10^-7 / 0.1 = 200 * 10^-7 = 2 * 10^-5 T.",
                "explanation": "\\(B = 2 \\times 10^{-5} \\text{ T}\\)."
            },
            {
                "id": "ex28-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 1.6 \\times 10^{-19} \\times 3 \\times 10^6 \\times 0.5 \\). What is \\( F \\times 10^{13} \\text{ N} \\)?",
                "answer": 2.4, "displayAnswer": "2.4 (F = 2.4×10⁻¹³ N)", "tolerance": 0.05, "unit": "",
                "hint": "1.6 * 1.5 = 2.4. -19 + 6 = -13.",
                "explanation": "\\(F = 2.4 \\times 10^{-13} \\text{ N}\\)."
            },
            {
                "id": "ex28-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "A proton and an electron move with the same speed in a uniform magnetic field. What is the ratio of their orbit radii \\( \\frac{r_p}{r_e} \\)? (\\( r = \\frac{mv}{qB} \\), \\( m_p \\approx 1840 m_e \\))",
                "answer": 1840, "displayAnswer": "1840", "tolerance": 50, "unit": "",
                "hint": "r is proportional to m for same v and q.",
                "explanation": "\\(\\frac{r_p}{r_e} = \\frac{m_p}{m_e} \\approx 1840\\)."
            },
            {
                "id": "ex28-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{1}{\\sqrt{4 \\times 10^{-6} \\times 2.5 \\times 10^{-5}}} \\)",
                "answer": 100000, "displayAnswer": "100,000 (or 10⁵)", "tolerance": 100, "unit": "",
                "hint": "4 * 2.5 = 10. 10 * 10^-11 = 10^-10. sqrt(10^-10) = 10^-5. Reciprocal is 10^5.",
                "explanation": "\\(\\frac{1}{10^{-5}} = 10^5 = 100,000\\)."
            },
            {
                "id": "ex28-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( 50 \\times 0.04 \\times 1.5 \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0.01, "unit": "",
                "hint": "2 * 1.5 = 3.",
                "explanation": "\\(50 \\times 0.04 = 2\\); \\(2 \\times 1.5 = 3\\)."
            },
            # Algebra (5)
            {
                "id": "ex28-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Cyclotron frequency is \\( f = \\frac{qB}{2\\pi m} \\). If \\( q = 1.6 \\times 10^{-19} \\text{ C} \\), \\( m = 1.6 \\times 10^{-27} \\text{ kg} \\), and \\( B = 1 \\text{ T} \\), find \\( f \\) in Mega-Hertz (MHz). (Use \\( 2\\pi \\approx 6.28 \\))",
                "answer": 15.9, "displayAnswer": "15.9", "tolerance": 0.5, "unit": "MHz",
                "hint": "(10^8) / 6.28 ≈ 1.59 * 10^7 Hz = 15.9 MHz.",
                "explanation": "\\(f = \\frac{10^8}{6.28} \\approx 15.9 \\text{ MHz}\\)."
            },
            {
                "id": "ex28-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Torque on a current loop is \\( \\tau = NIAB \\sin\\theta \\). If \\( N = 100 \\text{ turns} \\), \\( I = 2 \\text{ A} \\), area \\( A = 0.05 \\text{ m}^2 \\), \\( B = 0.4 \\text{ T} \\), and \\( \\theta = 30^\\circ \\), calculate \\( \\tau \\) in \\( \\text{N}\\cdot\\text{m} \\).",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "N·m",
                "hint": "100 * 2 * 0.05 * 0.4 * 0.5 = 10 * 0.2 = 2.",
                "explanation": "\\(\\tau = 100 \\times 2 \\times 0.05 \\times 0.4 \\times 0.5 = 2 \\text{ N}\\cdot\\text{m}\\)."
            },
            {
                "id": "ex28-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "A straight wire of length \\( L = 0.5 \\text{ m} \\) moves at speed \\( v = 4 \\text{ m/s} \\) perpendicular to magnetic field \\( B = 0.6 \\text{ T} \\). Using motional emf \\( e = B L v \\), find \\( e \\) in Volts.",
                "answer": 1.2, "displayAnswer": "1.2", "tolerance": 0.01, "unit": "V",
                "hint": "0.6 * 0.5 * 4 = 0.6 * 2 = 1.2 V.",
                "explanation": "\\(e = 0.6 \\times 0.5 \\times 4 = 1.2 \\text{ V}\\)."
            },
            {
                "id": "ex28-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Self-induced EMF is \\( e = -L\\frac{di}{dt} \\). If \\( L = 0.2 \\text{ H} \\) and current drops from \\( 5 \\text{ A} \\) to \\( 1 \\text{ A} \\) in \\( 0.02 \\text{ s} \\), find magnitude of induced EMF \\( e \\) in Volts.",
                "answer": 40, "displayAnswer": "40", "tolerance": 0.1, "unit": "V",
                "hint": "di/dt = 4 / 0.02 = 200 A/s. e = 0.2 * 200 = 40 V.",
                "explanation": "\\(e = 0.2 \\times \\frac{4}{0.02} = 40 \\text{ V}\\)."
            },
            {
                "id": "ex28-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Magnetic energy density in solenoid is \\( u_B = \\frac{B^2}{2\\mu_0} \\). If \\( B = 2 \\times 10^{-2} \\text{ T} \\) and \\( \\mu_0 = 4\\pi \\times 10^{-7} \\approx 1.256 \\times 10^{-6} \\), calculate \\( u_B \\) in \\( \\text{J/m}^3 \\) to nearest integer. (\\( \\frac{4 \\times 10^{-4}}{2.512 \\times 10^{-6}} \\))",
                "answer": 159, "displayAnswer": "159", "tolerance": 5, "unit": "J/m³",
                "hint": "400 / 2.512 ≈ 159.2 J/m^3.",
                "explanation": "\\(u_B \\approx 159 \\text{ J/m}^3\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex28-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Magnetic field at center of long solenoid is \\( B = \\mu_0 n I \\). If \\( n = 1000 \\text{ turns/m} \\), \\( I = 2 \\text{ A} \\), and \\( \\mu_0 = 4\\pi \\times 10^{-7} \\approx 1.257 \\times 10^{-6} \\), calculate \\( B \\times 10^3 \\text{ T} \\) (in milli-Tesla).",
                "answer": 2.51, "displayAnswer": "2.51", "tolerance": 0.05, "unit": "mT",
                "hint": "1.257*10^-6 * 1000 * 2 = 2.514 * 10^-3 T = 2.51 mT.",
                "explanation": "\\(B \\approx 2.51 \\text{ mT}\\)."
            },
            {
                "id": "ex28-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Force per unit length between two long parallel wires separated by \\( d = 0.2 \\text{ m} \\) carrying currents \\( I_1 = 10 \\text{ A} \\) and \\( I_2 = 20 \\text{ A} \\) is \\( \\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi d} \\). Calculate \\( \\frac{F}{L} \\times 10^4 \\text{ N/m} \\).",
                "answer": 2, "displayAnswer": "2 (F/L = 2×10⁻⁴ N/m)", "tolerance": 0.05, "unit": "",
                "hint": "(2*10^-7 * 10 * 20) / 0.2 = 400*10^-7 / 0.2 = 2000*10^-7 = 2*10^-4 N/m.",
                "explanation": "\\(\\frac{F}{L} = 2 \\times 10^{-4} \\text{ N/m}\\)."
            },
            {
                "id": "ex28-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A galvanometer has resistance \\( G = 50 \\text{ }\\Omega \\) and gives full scale deflection for \\( I_g = 2 \\text{ mA} \\). To convert it to an ammeter of range \\( I = 10 \\text{ A} \\), shunt resistance is \\( S \\approx \\frac{I_g G}{I} \\). Calculate \\( S \\) in \\( \\Omega \\).",
                "answer": 0.01, "displayAnswer": "0.01", "tolerance": 0.001, "unit": "Ω",
                "hint": "(0.002 * 50) / 10 = 0.1 / 10 = 0.01 Ω.",
                "explanation": "\\(S = \\frac{0.1}{10} = 0.01 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex28-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "To convert the same galvanometer (\\( G = 50 \\text{ }\\Omega, I_g = 2 \\text{ mA} \\)) into a voltmeter of range \\( V = 10 \\text{ V} \\), required series resistance is \\( R = \\frac{V}{I_g} - G \\). Find \\( R \\) in \\( \\Omega \\).",
                "answer": 4950, "displayAnswer": "4950", "tolerance": 5, "unit": "Ω",
                "hint": "10 / 0.002 - 50 = 5000 - 50 = 4950 Ω.",
                "explanation": "\\(R = 5000 - 50 = 4950 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex28-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Magnetic dipole moment of a revolving electron is Bohr Magneton \\( \\mu_B = \\frac{e\\hbar}{2m} \\approx 9.27 \\times 10^{-24} \\text{ A}\\cdot\\text{m}^2 \\). If magnetic field \\( B = 2 \\text{ T} \\), find maximum potential energy \\( U = \\mu_B B \\) in \\( 10^{-24} \\text{ J} \\).",
                "answer": 18.54, "displayAnswer": "18.54", "tolerance": 0.1, "unit": "",
                "hint": "9.27 * 2 = 18.54.",
                "explanation": "\\(U = 18.54 \\times 10^{-24} \\text{ J}\\)."
            }
        ]
    },
    {
        "id": 29,
        "title": "Exam-Level: Alternating Current & LCR Resonance",
        "subtitle": "Calculate impedance Z = √(R² + (XL - XC)²), resonance frequency, power factor, and transformer ratios.",
        "difficulty": 5,
        "tier": "Exam-Level",
        "estimatedMinutes": 25,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex29-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "In a series LCR circuit, \\( R = 40 \\text{ }\\Omega \\), \\( X_L = 100 \\text{ }\\Omega \\), and \\( X_C = 70 \\text{ }\\Omega \\). Calculate impedance \\( Z = \\sqrt{R^2 + (X_L - X_C)^2} \\) in \\( \\Omega \\).",
                "answer": 50, "displayAnswer": "50", "tolerance": 0, "unit": "Ω",
                "hint": "X_L - X_C = 30. sqrt(40^2 + 30^2) = 50 Ω.",
                "explanation": "\\(Z = \\sqrt{40^2 + 30^2} = 50 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex29-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "What is the power factor \\( \\cos\\phi = \\frac{R}{Z} \\) for this circuit (\\( R = 40 \\text{ }\\Omega, Z = 50 \\text{ }\\Omega \\))? Enter as decimal.",
                "answer": 0.8, "displayAnswer": "0.8", "tolerance": 0, "unit": "",
                "hint": "40 / 50 = 0.8.",
                "explanation": "\\(\\cos\\phi = \\frac{40}{50} = 0.8\\)."
            },
            {
                "id": "ex29-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Peak voltage of Indian domestic AC supply is \\( V_0 = \\sqrt{2} V_{\\text{rms}} \\). If \\( V_{\\text{rms}} = 220 \\text{ V} \\) and \\( \\sqrt{2} \\approx 1.414 \\), calculate \\( V_0 \\) to nearest integer.",
                "answer": 311, "displayAnswer": "311", "tolerance": 2, "unit": "V",
                "hint": "220 * 1.414 = 311.08 V.",
                "explanation": "\\(V_0 = 220 \\times 1.414 \\approx 311 \\text{ V}\\)."
            },
            {
                "id": "ex29-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Inductive reactance is \\( X_L = 2\\pi f L \\). If \\( f = 50 \\text{ Hz} \\) and \\( L = \\frac{0.7}{\\pi} \\text{ H} \\), calculate \\( X_L \\) in \\( \\Omega \\).",
                "answer": 70, "displayAnswer": "70", "tolerance": 0.1, "unit": "Ω",
                "hint": "2 * pi * 50 * (0.7 / pi) = 100 * 0.7 = 70 Ω.",
                "explanation": "\\(X_L = 100 \\times 0.7 = 70 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex29-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Capacitive reactance is \\( X_C = \\frac{1}{2\\pi f C} \\). If \\( f = 50 \\text{ Hz} \\) and \\( C = \\frac{100}{\\pi} \\text{ }\\mu\\text{F} \\), calculate \\( X_C \\) in \\( \\Omega \\).",
                "answer": 100, "displayAnswer": "100", "tolerance": 0.1, "unit": "Ω",
                "hint": "2 * pi * 50 * (100 / pi * 10^-6) = 100 * 100 * 10^-6 = 10^-2. 1 / 10^-2 = 100 Ω.",
                "explanation": "\\(X_C = \\frac{1}{10^{-2}} = 100 \\text{ }\\Omega\\)."
            },
            # Algebra (5)
            {
                "id": "ex29-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Resonant frequency of LCR circuit is \\( \\omega_0 = \\frac{1}{\\sqrt{LC}} \\). If \\( L = 0.25 \\text{ H} \\) and \\( C = 4 \\times 10^{-6} \\text{ F} \\), find \\( \\omega_0 \\) in rad/s.",
                "answer": 1000, "displayAnswer": "1000", "tolerance": 0.1, "unit": "rad/s",
                "hint": "LC = 10^-6. sqrt(10^-6) = 10^-3. omega_0 = 1 / 10^-3 = 1000 rad/s.",
                "explanation": "\\(\\omega_0 = \\frac{1}{10^{-3}} = 1000 \\text{ rad/s}\\)."
            },
            {
                "id": "ex29-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "For the same circuit, what is linear resonant frequency \\( f_0 = \\frac{\\omega_0}{2\\pi} \\) in Hz? (Use \\( 2\\pi \\approx 6.28 \\)) Enter to 1 decimal place.",
                "answer": 159.2, "displayAnswer": "159.2", "tolerance": 1, "unit": "Hz",
                "hint": "1000 / 6.28 ≈ 159.2 Hz.",
                "explanation": "\\(f_0 = \\frac{1000}{6.28} \\approx 159.2 \\text{ Hz}\\)."
            },
            {
                "id": "ex29-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Quality factor of series LCR circuit is \\( Q = \\frac{1}{R}\\sqrt{\\frac{L}{C}} \\). If \\( R = 10 \\text{ }\\Omega \\), \\( L = 0.25 \\text{ H} \\), and \\( C = 4 \\times 10^{-6} \\text{ F} \\), find \\( Q \\).",
                "answer": 25, "displayAnswer": "25", "tolerance": 0.1, "unit": "",
                "hint": "L/C = 0.25 / (4*10^-6) = 62500. sqrt(62500) = 250. Q = 250 / 10 = 25.",
                "explanation": "\\(Q = \\frac{250}{10} = 25\\)."
            },
            {
                "id": "ex29-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "A step-down transformer transforms \\( 2200 \\text{ V} \\) to \\( 220 \\text{ V} \\). If primary winding has \\( N_p = 5000 \\text{ turns} \\), find secondary turns \\( N_s = N_p \\frac{V_s}{V_p} \\).",
                "answer": 500, "displayAnswer": "500", "tolerance": 0, "unit": "",
                "hint": "5000 * (220 / 2200) = 5000 * 0.1 = 500 turns.",
                "explanation": "\\(N_s = 5000 \\times 0.1 = 500\\)."
            },
            {
                "id": "ex29-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "If secondary current is \\( I_s = 10 \\text{ A} \\) with \\( 100\\% \\) efficiency, find primary current \\( I_p = I_s \\frac{V_s}{V_p} \\) in Amperes.",
                "answer": 1, "displayAnswer": "1", "tolerance": 0, "unit": "A",
                "hint": "10 * (220 / 2200) = 1 A.",
                "explanation": "\\(I_p = 10 \\times 0.1 = 1 \\text{ A}\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex29-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Average AC power is \\( P_{\\text{avg}} = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi \\). If \\( V_{\\text{rms}} = 220 \\text{ V} \\), \\( I_{\\text{rms}} = 5 \\text{ A} \\), and \\( \\cos\\phi = 0.8 \\), calculate \\( P_{\\text{avg}} \\) in Watts.",
                "answer": 880, "displayAnswer": "880", "tolerance": 1, "unit": "W",
                "hint": "220 * 5 * 0.8 = 1100 * 0.8 = 880 W.",
                "explanation": "\\(P_{\\text{avg}} = 220 \\times 5 \\times 0.8 = 880 \\text{ W}\\)."
            },
            {
                "id": "ex29-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "At resonance in series LCR circuit, \\( X_L = X_C \\). What is the phase difference \\( \\phi \\) between current and voltage in degrees?",
                "answer": 0, "displayAnswer": "0°", "tolerance": 0, "unit": "°",
                "hint": "At resonance, tan(phi) = 0 => phi = 0.",
                "explanation": "\\(\\phi = 0^\\circ\\). Circuit is purely resistive at resonance."
            },
            {
                "id": "ex29-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "If \\( V(t) = 100 \\sin(100\\pi t) \\text{ V} \\), calculate the frequency \\( f = \\frac{\\omega}{2\\pi} \\) in Hz.",
                "answer": 50, "displayAnswer": "50", "tolerance": 0, "unit": "Hz",
                "hint": "100*pi / (2*pi) = 50 Hz.",
                "explanation": "\\(f = 50 \\text{ Hz}\\)."
            },
            {
                "id": "ex29-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "What is the rms voltage \\( V_{\\text{rms}} = \\frac{V_0}{\\sqrt{2}} \\) for this voltage (\\( V_0 = 100 \\text{ V} \\))? Enter to 1 decimal place. (\\( \\frac{100}{1.414} \\))",
                "answer": 70.7, "displayAnswer": "70.7", "tolerance": 0.5, "unit": "V",
                "hint": "100 * 0.707 = 70.7 V.",
                "explanation": "\\(V_{\\text{rms}} = 70.7 \\text{ V}\\)."
            },
            {
                "id": "ex29-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Wattless current is \\( I_{\\text{wattless}} = I_{\\text{rms}} \\sin\\phi \\). If \\( I_{\\text{rms}} = 10 \\text{ A} \\) and \\( \\cos\\phi = 0.8 \\) (so \\( \\sin\\phi = 0.6 \\)), find \\( I_{\\text{wattless}} \\) in Amperes.",
                "answer": 6, "displayAnswer": "6", "tolerance": 0.01, "unit": "A",
                "hint": "10 * 0.6 = 6 A.",
                "explanation": "\\(I_{\\text{wattless}} = 10 \\times 0.6 = 6 \\text{ A}\\)."
            }
        ]
    },
    {
        "id": 30,
        "title": "Exam-Level: NEET/JEE Grand Speed Challenge",
        "subtitle": "Comprehensive exam simulation: multi-step kinematics, optics, modern physics, and thermodynamics.",
        "difficulty": 5,
        "tier": "Exam-Level",
        "estimatedMinutes": 30,
        "questions": [
            # Mental Arithmetic (5)
            {
                "id": "ex30-q1", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "In radioactive decay, if \\( 15/16 \\) of sample decays in \\( 40 \\text{ minutes} \\), remaining fraction is \\( 1/16 = (1/2)^4 \\). What is the half-life \\( T_{1/2} \\) in minutes?",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "min",
                "hint": "4 half lives in 40 min => 40 / 4 = 10 min.",
                "explanation": "\\(T_{1/2} = \\frac{40}{4} = 10 \\text{ minutes}\\)."
            },
            {
                "id": "ex30-q2", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\frac{1.6 \\times 10^{-19} \\times 10^7}{3.2 \\times 10^{-12}} \\)",
                "answer": 0.5, "displayAnswer": "0.5", "tolerance": 0.01, "unit": "",
                "hint": "(1.6 / 3.2) * 10^(-19 + 7 - (-12)) = 0.5 * 10^0 = 0.5.",
                "explanation": "\\(0.5 \\times 10^0 = 0.5\\)."
            },
            {
                "id": "ex30-q3", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\sqrt{1.44 \\times 10^8} \\)",
                "answer": 12000, "displayAnswer": "12,000 (or 1.2×10⁴)", "tolerance": 10, "unit": "",
                "hint": "1.2 * 10^4 = 12000.",
                "explanation": "\\(1.2 \\times 10^4 = 12,000\\)."
            },
            {
                "id": "ex30-q4", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Evaluate: \\( \\frac{6.63 \\times 10^{-34} \\times 3 \\times 10^8}{5 \\times 10^{-7}} \\times 10^{19} \\). What is energy in Joules multiplied by \\( 10^{19} \\)? Enter to 2 decimal places.",
                "answer": 3.98, "displayAnswer": "3.98", "tolerance": 0.1, "unit": "",
                "hint": "(19.89 / 5) = 3.978. -34 + 8 - (-7) + 19 = 0.",
                "explanation": "\\(\\frac{19.89}{5} = 3.978 \\approx 3.98\\)."
            },
            {
                "id": "ex30-q5", "section": "mental", "sectionName": "Mental Arithmetic", "type": "numeric",
                "question": "Calculate: \\( \\tan 45^\\circ + \\sin 90^\\circ + \\cos 0^\\circ \\)",
                "answer": 3, "displayAnswer": "3", "tolerance": 0, "unit": "",
                "hint": "1 + 1 + 1 = 3.",
                "explanation": "\\(1 + 1 + 1 = 3\\)."
            },
            # Algebra (5)
            {
                "id": "ex30-q6", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "In a potentiometer experiment, balance length with cell of EMF \\( E_1 = 1.5 \\text{ V} \\) is \\( l_1 = 60 \\text{ cm} \\). If another cell balances at \\( l_2 = 80 \\text{ cm} \\), calculate \\( E_2 = E_1 \\frac{l_2}{l_1} \\) in Volts.",
                "answer": 2, "displayAnswer": "2", "tolerance": 0.01, "unit": "V",
                "hint": "1.5 * (80 / 60) = 1.5 * (4/3) = 2 V.",
                "explanation": "\\(E_2 = 1.5 \\times \\frac{4}{3} = 2 \\text{ V}\\)."
            },
            {
                "id": "ex30-q7", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Internal resistance is \\( r = R\\left(\\frac{l_1}{l_2} - 1\\right) \\). If open circuit length \\( l_1 = 75 \\text{ cm} \\), shunted with \\( R = 10 \\text{ }\\Omega \\) balances at \\( l_2 = 60 \\text{ cm} \\), find \\( r \\) in \\( \\Omega \\).",
                "answer": 2.5, "displayAnswer": "2.5", "tolerance": 0.01, "unit": "Ω",
                "hint": "10 * (75/60 - 1) = 10 * (1.25 - 1) = 10 * 0.25 = 2.5 Ω.",
                "explanation": "\\(r = 10 \\times 0.25 = 2.5 \\text{ }\\Omega\\)."
            },
            {
                "id": "ex30-q8", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "Doppler effect for sound: source moves toward stationary observer at \\( v_s = 34 \\text{ m/s} \\). Speed of sound \\( v = 340 \\text{ m/s} \\). If source frequency \\( f_0 = 900 \\text{ Hz} \\), calculate observed frequency \\( f' = f_0 \\left(\\frac{v}{v - v_s}\\right) \\) in Hz.",
                "answer": 1000, "displayAnswer": "1000", "tolerance": 1, "unit": "Hz",
                "hint": "900 * (340 / 306) = 900 * (10 / 9) = 1000 Hz.",
                "explanation": "\\(f' = 900 \\times \\frac{10}{9} = 1000 \\text{ Hz}\\)."
            },
            {
                "id": "ex30-q9", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "A particle executes SHM with equation \\( x = 10 \\sin(4t) \\text{ cm} \\). What is its maximum velocity \\( v_{\\text{max}} = A\\omega \\) in \\( \\text{cm/s} \\)?",
                "answer": 40, "displayAnswer": "40", "tolerance": 0, "unit": "cm/s",
                "hint": "10 * 4 = 40 cm/s.",
                "explanation": "\\(v_{\\text{max}} = 10 \\times 4 = 40 \\text{ cm/s}\\)."
            },
            {
                "id": "ex30-q10", "section": "algebra", "sectionName": "Algebra", "type": "numeric",
                "question": "What is its maximum acceleration magnitude \\( a_{\\text{max}} = A\\omega^2 \\) in \\( \\text{cm/s}^2 \\)?",
                "answer": 160, "displayAnswer": "160", "tolerance": 0, "unit": "cm/s²",
                "hint": "10 * 16 = 160 cm/s^2.",
                "explanation": "\\(a_{\\text{max}} = 10 \\times 16 = 160 \\text{ cm/s}^2\\)."
            },
            # Physics Calculations (5)
            {
                "id": "ex30-q11", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Charging time constant of an RC circuit is \\( \\tau = RC \\). If \\( R = 2 \\times 10^6 \\text{ }\\Omega \\) and \\( C = 5 \\times 10^{-6} \\text{ F} \\), calculate \\( \\tau \\) in seconds.",
                "answer": 10, "displayAnswer": "10", "tolerance": 0, "unit": "s",
                "hint": "2*10^6 * 5*10^-6 = 10 s.",
                "explanation": "\\(\\tau = 10 \\text{ s}\\)."
            },
            {
                "id": "ex30-q12", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "A capacitor is charged to \\( V_0 = 100 \\text{ V} \\). After 1 time constant (\\( t = \\tau \\)), voltage across capacitor is \\( V = V_0 (1 - e^{-1}) \\approx 0.632 V_0 \\). What is \\( V \\) in Volts?",
                "answer": 63.2, "displayAnswer": "63.2", "tolerance": 0.5, "unit": "V",
                "hint": "100 * 0.632 = 63.2 V.",
                "explanation": "\\(V = 63.2 \\text{ V}\\)."
            },
            {
                "id": "ex30-q13", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Calculate de Broglie wavelength of an alpha particle (mass \\( 6.64 \\times 10^{-27} \\text{ kg} \\)) accelerated through \\( V = 100 \\text{ V} \\): \\( \\lambda = \\frac{0.101}{\\sqrt{V}} \\text{ \\AA} \\). Enter \\( \\lambda \\) in Angstroms.",
                "answer": 0.0101, "displayAnswer": "0.0101", "tolerance": 0.001, "unit": "Å",
                "hint": "0.101 / 10 = 0.0101 Å.",
                "explanation": "\\(\\lambda = \\frac{0.101}{10} = 0.0101 \\text{ \\AA}\\)."
            },
            {
                "id": "ex30-q14", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "In a nuclear fission of U-235, ~200 MeV energy is released per fission. How many fissions per second produce a reactor power of \\( 3.2 \\text{ MW} = 3.2 \\times 10^6 \\text{ W} \\)? (\\( 200 \\text{ MeV} = 3.2 \\times 10^{-11} \\text{ J} \\)). What is \\( N \\times 10^{-17} \\)?",
                "answer": 1, "displayAnswer": "1 (N = 10¹⁷ fissions/s)", "tolerance": 0.05, "unit": "",
                "hint": "(3.2 * 10^6) / (3.2 * 10^-11) = 10^17.",
                "explanation": "\\(N = \\frac{3.2 \\times 10^6}{3.2 \\times 10^{-11}} = 10^{17} \\text{ fissions/s}\\)."
            },
            {
                "id": "ex30-q15", "section": "physics", "sectionName": "Physics-Style Calculations", "type": "numeric",
                "question": "Congratulations on completing all 30 days! Calculate your target exam calculation speed: solving 45 NEET physics questions in 45 minutes = 1 minute per question. What is 60 seconds / 1 question in seconds per question?",
                "answer": 60, "displayAnswer": "60 seconds", "tolerance": 0, "unit": "s",
                "hint": "60 seconds.",
                "explanation": "60 seconds per question with high accuracy is the gold standard for top NEET/JEE ranks!"
            }
        ]
    }
]

print(f"Tier 6 loaded: {len(tier6)} exercises.")
