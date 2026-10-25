import os
import functools
from pathlib import Path

include_list = ['2013/2014', '2014/2015', '2015/2016', '2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021', '2021/2022', '2022/2023', '2023/2024', '2024/2025', '2025/2026']
local_prefix = "" # "../"
prefix_length = 5 # 8

def processFileName(path):
    with open(path, "r") as fl:
        fl_content = list(fl)
        fl_content = list(filter(lambda x: x.strip().startswith('#'), fl_content))
        if len(fl_content) == 0:
            return ""
        return fl_content[0].strip()[2:]

def processTakprogContest(path): 
    taskList = []
    with os.scandir(path) as tasks:
        for task in tasks:
            if task.is_file() and task.name.endswith('.md'):
                taskList.append((processFileName(task.path), task.path[prefix_length:]))
    return taskList

def processTakprogSeason(path): 
    contestDict = {}
    with os.scandir(path) as contests:
        for contest in contests:
            if contest.is_dir():
                contestDict[contest.name] = processTakprogContest(contest.path)
    return contestDict

def task_compare(x, y):
    def task_key(task):
        name = task[0]
        prefix = name.split(' - ')[0]
        if len(prefix) > 1 and prefix[0] == 'B' and prefix[1:].isdigit():
            return (0, int(prefix[1:]), name)
        if len(prefix) > 1 and prefix[0] == 'A' and prefix[1:].isdigit():
            return (1, int(prefix[1:]), name)
        if prefix.isdigit():
            return (0, int(prefix), name)
        return (2, 0, name)

    x_key = task_key(x)
    y_key = task_key(y)

    if x_key == y_key: 
        return 0
    if x_key < y_key:
        return -1
    return +1

def writeSeasonOverview(seasons):
    rounds = {
        'kv1': 'Kvalifikacije 1', 'kv2': 'Kvalifikacije 2',
        'kv3': 'Kvalifikacije 3', 'okr': 'Okružno', 'drz': 'Državno',
        'sio': 'SIO', 'piz': 'PIZ', 'izb': 'Izborno',
        'ejoi_izb': 'EJOI izborno', 'egoi_izb': 'EGOI izborno',
    }
    lines = ['<div class="archive-seasons" markdown>', '']
    for season in sorted(seasons, reverse=True):
        if season not in include_list:
            continue
        links = []
        for key, label in rounds.items():
            tasks = seasons[season].get(key, [])
            if not tasks:
                continue
            first = sorted(tasks, key=functools.cmp_to_key(task_compare))[0]
            path = Path(first[1]).relative_to('takprog').as_posix()
            if key == 'kv1' and not seasons[season].get('kv2'):
                label = 'Kvalifikacije'
            links.append(f'[{label}]({path})')
        if links:
            lines.extend([
                '<section class="archive-season" markdown>', '',
                f'### {season}', '', ' '.join(links), '', '</section>', '',
            ])
    lines.append('</div>')
    overview = Path(local_prefix + 'docs/takprog/index.md')
    before, rest = overview.read_text().split('<!-- seasons:start -->', 1)
    _, after = rest.split('<!-- seasons:end -->', 1)
    overview.write_text(before + '<!-- seasons:start -->\n\n' +
                       '\n'.join(lines) + '\n\n<!-- seasons:end -->' + after)


def processTakprog(nav): 
    prefix = local_prefix + "docs/takprog"
    seasons = {}
    with os.scandir(prefix) as years:
        for season in years:
            if season.is_dir():
                seasons[season.name.replace('_','/')] = processTakprogSeason(season.path)

    sorted_keys = list(seasons.keys())
    sorted_keys.sort()
    for key1 in sorted_keys:
        if key1 in include_list:
            nav.write("  - "+key1+'\n')
            if 'kv1' in seasons[key1].keys():
                if 'kv2' in seasons[key1].keys():
                    nav.write("    - Kvalifikacije 1\n")
                else:
                    nav.write("    - Kvalifikacije\n")
                key2 = 'kv1'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'kv2' in seasons[key1].keys():
                nav.write("    - Kvalifikacije 2\n")
                key2 = 'kv2'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'kv3' in seasons[key1].keys():
                nav.write("    - Kvalifikacije 3\n")
                key2 = 'kv3'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'okr' in seasons[key1].keys():
                nav.write("    - Okružno\n")
                key2 = 'okr'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'drz' in seasons[key1].keys():
                nav.write("    - Državno\n")
                key2 = 'drz'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'sio' in seasons[key1].keys():
                nav.write("    - SIO\n")
                key2 = 'sio'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'piz' in seasons[key1].keys():
                nav.write("    - Kvalifikaciono za izborno (PIZ)\n")
                key2 = 'piz'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'izb' in seasons[key1].keys():
                nav.write("    - Izborno\n")
                key2 = 'izb'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'ejoi_izb' in seasons[key1].keys():
                nav.write("    - EJOI izborno\n")
                key2 = 'ejoi_izb'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")
            if 'egoi_izb' in seasons[key1].keys():
                nav.write("    - EGOI izborno\n")
                key2 = 'egoi_izb'
                seasons[key1][key2] = sorted(seasons[key1][key2], key=functools.cmp_to_key(task_compare))
                for key3 in seasons[key1][key2]:
                    nav.write("      - ["+key3[0]+"]("+key3[1]+")\n")

    writeSeasonOverview(seasons)


print(os.getcwd())
with open(local_prefix + "docs/nav.md", "w") as nav:
    nav.write("---\n")
    nav.write("search:\n")
    nav.write("  exclude: true\n")
    nav.write("---\n")
    nav.write("\n")

    nav.write("- [Početna](index.md)\n")
    nav.write("- Arhiva takmičenja\n")
    nav.write("  - [Pregled sezona](takprog/index.md)\n")
    processTakprog(nav)
    nav.write("- [Materijali](materijali.md)\n")
    nav.write("- [O arhivi](o-arhivi.md)\n")
