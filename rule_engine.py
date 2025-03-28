"""
基础规则引擎实现
包含5条基础项目验证规则：
1. 项目类型必须在绿色目录中
2. 预算范围检查
3. 项目周期检查
4. 必填字段检查
5. 开始日期检查
"""

class RuleEngine:
    def __init__(self):
        self.green_categories = ["环保", "新能源", "可持续发展"]  # 示例规则数据

    def check_green_category(self, project_data):
        """检查项目类型是否在绿色目录中"""
        project_type = project_data.get("project_type")
        if project_type not in self.green_categories:
            return False, f"项目类型'{project_type}'不符合绿色要求"
        return True, ""


class RuleEngine:
    def __init__(self):
        # 初始化可能需要的数据
        self.green_categories = ["环保", "新能源", "可持续发展"]  # 示例绿色目录

    def check_all_rules(self, project_data):
        """
        检查所有规则的入口函数
        :param project_data: 包含项目信息的字典
        :return: (是否通过, 失败原因) 元组
        """
        rules = [
            self.check_green_category,
            # 这里添加其他规则函数
        ]

        for rule in rules:
            passed, message = rule(project_data)
            if not passed:
                return False, message

        return True, "所有规则检查通过"

def check_green_category(self, project_data):
    """
    规则1: 项目类型必须在绿色目录中
    """
    project_type = project_data.get("project_type")
    if project_type not in self.green_categories:
        return False, f"项目类型'{project_type}'不在绿色目录中"
    return True, ""

def check_green_category(self, project_data):
    """
    规则1: 项目类型必须在绿色目录中
    """
    project_type = project_data.get("project_type")
    if project_type not in self.green_categories:
        return False, f"项目类型'{project_type}'不在绿色目录中"
    return True, ""