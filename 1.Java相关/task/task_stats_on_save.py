import re

# 使用绝对路径，替换成你自己的真实路径
file_path = r"A:\01 找工作\01 线上实习\retail-management-system\retail-management-system\docs\0.学习笔记\1.Java相关\task\task_list.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

completed = len(re.findall(r"- \[x\]", content, flags=re.IGNORECASE))
total = len(re.findall(r"- \[( |x)\]", content, flags=re.IGNORECASE))
progress = completed / total * 100 if total > 0 else 0

result = (
    f"Completed tasks: {completed}\n"
    f"Total tasks: {total}\n"
    f"Progress: {progress:.2f}%\n"
)

print(result)

