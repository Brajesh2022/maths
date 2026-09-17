import json
import data_tier1
import data_tier2
import data_tier3
import data_tier4
import data_tier5
import data_tier6

all_exercises = (
    data_tier1.tier1 +
    data_tier2.tier2 +
    data_tier3.tier3 +
    data_tier4.tier4 +
    data_tier5.tier5 +
    data_tier6.tier6
)

print(f"Total exercises loaded: {len(all_exercises)}")

# Validation checks
assert len(all_exercises) == 30, f"Expected 30 exercises, got {len(all_exercises)}"

seen_qids = set()
total_questions = 0

for i, ex in enumerate(all_exercises, start=1):
    assert ex["id"] == i, f"Exercise ID mismatch at index {i}: got {ex['id']}"
    assert "title" in ex and len(ex["title"]) > 0
    assert "subtitle" in ex and len(ex["subtitle"]) > 0
    assert "difficulty" in ex and 1 <= ex["difficulty"] <= 5
    assert len(ex["questions"]) == 15, f"Exercise {i} has {len(ex['questions'])} questions, expected 15"
    
    sections_count = {"mental": 0, "algebra": 0, "physics": 0}
    
    for q in ex["questions"]:
        total_questions += 1
        qid = q["id"]
        assert qid not in seen_qids, f"Duplicate Question ID: {qid}"
        seen_qids.add(qid)
        
        sec = q["section"]
        assert sec in sections_count, f"Invalid section: {sec} in {qid}"
        sections_count[sec] += 1
        
        qtype = q["type"]
        assert qtype in ["numeric", "mcq"], f"Invalid type: {qtype} in {qid}"
        
        assert "question" in q and len(q["question"]) > 0, f"Empty question in {qid}"
        assert "answer" in q, f"Missing answer in {qid}"
        assert "displayAnswer" in q and len(str(q["displayAnswer"])) > 0, f"Missing displayAnswer in {qid}"
        assert "explanation" in q and len(q["explanation"]) > 0, f"Missing explanation in {qid}"
        
        if qtype == "mcq":
            assert "options" in q, f"MCQ missing options in {qid}"
            assert len(q["options"]) == 4, f"MCQ options must have 4 items in {qid}, got {len(q['options'])}"
            assert isinstance(q["answer"], int) and 0 <= q["answer"] < 4, f"MCQ answer must be 0..3 in {qid}, got {q['answer']}"
        else:
            assert isinstance(q["answer"], (int, float)), f"Numeric answer must be number in {qid}, got {type(q['answer'])}"
            assert "tolerance" in q, f"Numeric question missing tolerance in {qid}"
    
    assert sections_count["mental"] == 5, f"Exercise {i} has {sections_count['mental']} mental questions (expected 5)"
    assert sections_count["algebra"] == 5, f"Exercise {i} has {sections_count['algebra']} algebra questions (expected 5)"
    assert sections_count["physics"] == 5, f"Exercise {i} has {sections_count['physics']} physics questions (expected 5)"

assert total_questions == 450, f"Expected 450 questions total, got {total_questions}"
print("All 450 questions and 30 exercises PASSED strict validation!")

# Write to questions.js
js_content = "/**\n * 30-Day Math & Calculation Training Data\n * 30 Exercises x 15 Questions = 450 Questions Total\n */\n"
js_content += "const EXERCISES_DATA = " + json.dumps(all_exercises, indent=2) + ";\n"
js_content += "if (typeof module !== 'undefined' && module.exports) { module.exports = EXERCISES_DATA; }\n"

with open("/data/data/com.termux/files/home/maths_2026-09-17_18-35/questions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated questions.js ({len(js_content)} bytes)")
