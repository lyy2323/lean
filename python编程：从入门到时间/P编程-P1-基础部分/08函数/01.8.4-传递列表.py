def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个涉及，知道没有未打印的涉及未知
    打印每个涉及后，都将其移动到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"正在打印:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    """
    print("\n这是打印好的:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)