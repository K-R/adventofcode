def is_safe_report(report: list[int]) -> int | None:
    is_decreasing = True
    is_increasing = True
    for index, level in enumerate(report):
        has_next_level = index < len(report) - 1

        if not has_next_level:
            continue

        next_level = report[index + 1]

        is_decreasing = level > next_level

        if is_decreasing == is_increasing and index > 0:
            return False

        is_increasing = level < next_level

        if not is_decreasing and not is_increasing or is_decreasing and is_increasing:
            return False

        difference = level - next_level if is_decreasing else next_level - level
        if difference > 3:
            return False
    
    return True

with open("input/02.txt") as file:
    reports = []
    for line in file.readlines():
        report = [int(level) for level in line.split()]
        reports.append(report)

total_safe_reports = 0
for report in reports:
    if is_safe_report(report):
        total_safe_reports += 1
        continue

    for index in range(len(report)):
        new_report = list(report)
        new_report.pop(index)
        if is_safe_report(new_report):
            total_safe_reports += 1
            break
