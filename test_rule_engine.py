from rule_engine import RuleEngine


def test_rule_engine():
    engine = RuleEngine()

    # 测试用例1: 完美数据
    good_data = {
        "project_name": "太阳能项目",
        "project_type": "新能源",
        "budget": 500000,
        "duration_months": 12,
        "start_date": "2024-01-01"
    }
    print(engine.check_all_rules(good_data))  # 应返回(True, "所有规则检查通过")

    # 测试用例2: 类型不在绿色目录
    bad_type_data = {
        "project_name": "煤炭项目",
        "project_type": "传统能源",
        # ...其他字段
    }
    print(engine.check_all_rules(bad_type_data))  # 应返回False和相应错误信息

    # 添加更多测试用例...