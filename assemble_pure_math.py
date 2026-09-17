import json
import math_days_1_10
import math_days_11_20
import math_days_21_30

all_days = math_days_1_10.days_1_10 + math_days_11_20.days_11_20 + math_days_21_30.days_21_30

print(f"Total exercises assembled: {len(all_days)}")
assert len(all_days) == 30, f"Expected 30 exercises, found {len(all_days)}"

total_questions = 0
for idx, day in enumerate(all_days):
    day_num = idx + 1
    day["id"] = day_num
    if "estimatedMinutes" not in day:
        day["estimatedMinutes"] = 15
    q_len = len(day['questions'])
    assert q_len == 15, f"Day {day_num} has {q_len} questions"
    sec_counts = {}
    for q_idx, q in enumerate(day["questions"]):
        total_questions += 1
        sec_name = q["sectionName"]
        sec_counts[sec_name] = sec_counts.get(sec_name, 0) + 1
        assert q["answer"] is not None, f"Null answer in Day {day_num} Q{q_idx+1}"
        assert q["question"], f"Empty question in Day {day_num} Q{q_idx+1}"
        assert q["explanation"], f"Empty explanation in Day {day_num} Q{q_idx+1}"
    
    expected_sections = [
        "Mental Arithmetic",
        "Fractions & Decimals",
        "Powers, Roots & Surds",
        "Algebra & Equations",
        "Scientific Notation & Estimation"
    ]
    for es in expected_sections:
        count = sec_counts.get(es, 0)
        assert count == 3, f"Day {day_num} has {count} questions for section '{es}', expected 3"

assert total_questions == 450, f"Expected 450 questions, found {total_questions}"
print("Validation successful: Exactly 30 exercises, 450 questions (15 per day, 3 per section).")

js_content = "/**\n * 30-Day Math & Calculation Training Data\n * 30 Exercises x 15 Questions = 450 Questions Total (Pure Mathematics & Calculations)\n */\n"
js_content += "const EXERCISES_DATA = " + json.dumps(all_days, indent=2, ensure_ascii=False) + ";\n\n"
js_content += "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = EXERCISES_DATA;\n}\n"

with open("questions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated questions.js ({len(js_content)} bytes).")
