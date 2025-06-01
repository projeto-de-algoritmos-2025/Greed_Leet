import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap = []
        fuel = startFuel
        i = 0
        refuels = 0

        while fuel < target:
            while i < len(stations) and stations[i][0] <= fuel:
                # Armazenamos como negativo para simular uma max-heap com heapq
                heapq.heappush(max_heap, -stations[i][1])
                i += 1

            if not max_heap:
                return -1

            # Reabastece com o posto de maior combustível disponível até agora
            fuel += -heapq.heappop(max_heap)
            refuels += 1

        return refuels
if __name__ == "__main__":
    sol = Solution()
    target = 100
    startFuel = 10
    stations = [[10,60], [20,30], [30,30], [60,40]]

    resultado = sol.minRefuelStops(target, startFuel, stations)
    print("=== Teste: Problema 871 ===")
    print(f"Target: {target}")
    print(f"StartFuel: {startFuel}")
    print(f"Stations: {stations}")
    print(f"Saída obtida  : {resultado}")
