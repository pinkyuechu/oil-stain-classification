for rule in app.url_map.iter_rules():
    print(rule.endpoint, rule.rule)