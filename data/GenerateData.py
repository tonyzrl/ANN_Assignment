import csv
import random

# Task data: ID, Estimated Time, Difficulty, Deadline, Skill Required
tasks = [{"id": "T1", "estimated_time": 4, "difficulty": 3, "deadline": 8, "skill_required": "A"},
        {"id": "T2", "estimated_time": 6, "difficulty": 5, "deadline": 12, "skill_required": "B"},
        {"id": "T3", "estimated_time": 2, "difficulty": 2, "deadline": 6, "skill_required": "A"},
        {"id": "T4", "estimated_time": 5, "difficulty": 4, "deadline": 10, "skill_required": "C"},
        {"id": "T5", "estimated_time": 3, "difficulty": 1, "deadline": 7, "skill_required": "A"},
        {"id": "T6", "estimated_time": 8, "difficulty": 6, "deadline": 15, "skill_required": "B"},
        {"id": "T7", "estimated_time": 4, "difficulty": 3, "deadline": 9, "skill_required": "C"},
        {"id": "T8", "estimated_time": 7, "difficulty": 5, "deadline": 14, "skill_required": "B"},
        {"id": "T9", "estimated_time": 2, "difficulty": 2, "deadline": 5, "skill_required": "A"},
        {"id": "T10", "estimated_time": 6, "difficulty": 4, "deadline": 11, "skill_required": "C"},]

# Employee data: ID, Available hours, Skill level, Skills
employees = [{"id": "E1", "hours_avail": 10, "skill_level": 4, "skills": ["A", "C"]},
            {"id": "E2", "hours_avail": 12, "skill_level": 6, "skills": ["A", "B", "C"]},
            {"id": "E3", "hours_avail": 8, "skill_level": 3, "skills": ["A"]},
            {"id": "E4", "hours_avail": 15, "skill_level": 7, "skills": ["B", "C"]},
            {"id": "E5", "hours_avail": 9, "skill_level": 5, "skills": ["A", "C"]}]

def generate_assignments_csv(seed):
    num_samples=100
    output_file="assignment_output.csv"
    
    num_employees = len(employees)
    num_tasks = len(tasks)

    # Map index to employee ID (0 → E1, 1 → E2, ...)
    emp_id_map = {i: emp["id"] for i, emp in enumerate(employees)}

    # Set random seed
    random.seed(seed)

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        for _ in range(num_samples):
            # Generate a random assignment
            assignment = [random.randint(0, num_employees - 1) for _ in range(num_tasks)]
            penalty = evaluate_penalty(tasks, employees, assignment)

            # Convert employee indices to readable IDs
            assignment_ids = [emp_id_map[emp_idx] for emp_idx in assignment]

            # Append penalty cost
            row = assignment_ids + [penalty]
            writer.writerow(row)

    print(f"{num_samples} seeded task-employee assignments saved to '{output_file}'.")

def evaluate_penalty(tasks, employees, assignment):
    ALPHA = 0.20
    BETA = 0.20
    DELTA = 0.20
    GAMMA = 0.20
    SIGMA = 0.20
    
    overload_violation = 0.0
    skill_mismatch_violation = 0.0
    difficulty_violation = 0.0
    deadline_violation = 0.0
    unique_violation = 0.0

    # Initialise lists for tracking employee work time and tasks
    hours_assigned = [0] * len(employees)
    employee_tasks = [[] for _ in range(len(employees))]
    
    # Initialise list for tracking number of task assignments
    task_counts = [0] * len(tasks)

    for t_idx, emp_idx in enumerate(assignment):
        task_counts[t_idx] += 1
        task = tasks[t_idx]
        emp = employees[emp_idx]

        # Accumulate employee work time
        hours_assigned[emp_idx] += task["estimated_time"]
        employee_tasks[emp_idx].append((t_idx, task))

        # Finding skill mismatch violation
        if task["skill_required"] not in emp["skills"]:
            skill_mismatch_violation += 1

        # Finding difficulty violation
        if emp["skill_level"] < task["difficulty"]:
            difficulty_violation += 1

    # Finding unique assignment violation
    for count in task_counts:
        if count != 1:
            unique_violation += abs(1 - count)  # Penalise if not assigned exactly once

    # Finding overload violation
    for emp_idx, total_hours in enumerate(hours_assigned):
        if total_hours > employees[emp_idx]["hours_avail"]:
            overload_violation += total_hours - employees[emp_idx]["hours_avail"]

    # Finding deadline violation
    for emp_idx, tasks in enumerate(employee_tasks):
        sorted_tasks = sorted(tasks, key=lambda t: t[1]["estimated_time"])  # Sort by task duration
        finish_time = 0
        for t_idx, task in sorted_tasks:
            finish_time += task["estimated_time"]
            if finish_time > task["deadline"]:
                deadline_violation += finish_time - task["deadline"]

    # Calculate cost for solution
    cost = (ALPHA * overload_violation + BETA * skill_mismatch_violation +
            DELTA * difficulty_violation + GAMMA * deadline_violation +
            SIGMA * unique_violation)
    
    return cost

if __name__ == '__main__':
    seed = input("Enter seed for task-assignment data generation: ")
    generate_assignments_csv(seed)