def solve(teams):
    teams = teams.split('\n')[:-1]

    hosts, guests = [], []
    for team in teams:
        host, guest =team.split()
        hosts.append(host)
        guests.append(guest)

    count = 0
    for host in hosts:
        count += guests.count(host)

    return count


if __name__ == '__main__':
    teams = ''
    for i in range(int(input())):
        teams += input() + '\n'
 
    print(solve(teams))


def test():
    assert solve('''1 2
2 4
3 4
''') == 1
    assert solve('''100 42
42 100
5 42
100 5
''') == 5
