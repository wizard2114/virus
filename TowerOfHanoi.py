def tower_of_hanoi(n, source, spare , destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, spare)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, spare, source, destination)

tower_of_hanoi(3, 'A', 'B', 'C')
