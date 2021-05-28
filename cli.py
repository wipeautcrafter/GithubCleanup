from datetime import datetime
from PyInquirer import prompt


def repo_choices(repos):
    old = [r for r in repos if weeks_since(r.pushed_at) > 3]
    mapped = [{
        "name": f"{r.full_name} ({weeks_since(r.pushed_at)} weeks old)",
        "value": r
    } for r in old]

    return mapped


def repos_prompt(repos):
    choices = repo_choices(repos)

    properties = [{
        "type": "checkbox",
        "name": "repositories",
        "message": "Select Repositories:",
        "choices": choices
    }]

    answers = prompt(properties)
    chosen = answers['repositories']
    amount = len(chosen)

    if amount == 0:
        print("\nNo repositories have been chosen.")
        return []

    print("\nRepositories marked for deletion:")
    [print(f" \u2192 {c.full_name}") for c in chosen]
    print("")  # ugly newline

    return chosen


def repo_prompt(repo):
    properties = [{
        "type": "confirm",
        "name": "confirm",
        "default": False,
        "message": f"Are you sure you want to remove {repo.full_name}?"
    }]

    answer = prompt(properties)
    confirm = answer['confirm']

    if not confirm:
        print(f" \u00D7 keeping {repo.full_name}")
        return False

    print(f" \u2713 removing {repo.full_name}")
    return True


def weeks_since(date):
    return round((datetime.now() - date).days / 7)
