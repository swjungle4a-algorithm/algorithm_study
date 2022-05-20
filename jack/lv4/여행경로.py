def dfs(answer, graph_tickets, route, ticket_cnt, departure, cnt) :
    if cnt == ticket_cnt :
        answer.append(route[:])
        return
    for idx, ticket in enumerate(graph_tickets[departure]) :
        arrival, isUsed = ticket
        if isUsed :
            continue
        graph_tickets[departure][idx][1] = 1
        route.append(arrival)
        dfs(answer, graph_tickets, route, ticket_cnt, arrival, cnt+1)
        graph_tickets[departure][idx][1] = 0
        route.pop()
    
def solution(tickets):
    answer = []
    
    airports = set()
    for a1, a2 in tickets :
        airports.add(a1)
        airports.add(a2)
    graph_tickets = {airport : [] for airport in airports}
    
    for departure, arrival in tickets :
        graph_tickets[departure].append([arrival,0])
    
    for i in graph_tickets :
        graph_tickets[i].sort()
    
    dfs(answer, graph_tickets, ["ICN"], len(tickets), "ICN", 0)
    
    return answer[0]
