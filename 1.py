def calculate_event_driven(A, B, bandwidth_bytes_per_sec=125000):
    """
    Kiszámítja az eseményvezérelt rendszer kapacitását
    """
    message_size = 7  # 2 bájt adat + 5 bájt overhead
    total_message_size = 8  # üzenet + 1 bájt szünet
    
    # Egy üzenet továbbítási ideje milliszekundumban
    message_time_ms = (total_message_size / bandwidth_bytes_per_sec) * 1000
    
    # B milliszekundum alatt küldhető üzenetek száma
    max_messages = int(B / message_time_ms)
    
    return max_messages, message_time_ms

def calculate_time_driven(A, B):
    """
    Kiszámítja az idővezérelt rendszer minimális sávszélesség igényét
    """
    total_variables = A * B
    
    # Egy körben küldendő bájtok száma
    bytes_per_round = (total_variables * 7) + (total_variables - 1)
    
    # B msec alatt küldendő bájtok másodpercenként
    bytes_per_sec = bytes_per_round * (1000 / B)
    
    # Átváltás Mbit/sec-re
    bandwidth_mbits = (bytes_per_sec * 8) / 1_000_000
    
    return bandwidth_mbits, bytes_per_round, bytes_per_sec

def print_results(A, B):
    """
    Részletes eredmények kiírása a számítások menetével együtt
    """
    print(f"\nSzámítások A={A} és B={B} paraméterekkel:")
    print("=" * 60)
    
    # 1.1 Eseményvezérelt számítások
    print("\n1.1 ESEMÉNYVEZÉRELT MŰKÖDÉS")
    print("-" * 60)
    max_events, message_time = calculate_event_driven(A, B)
    
    print(f"Adatok:")
    print(f"- Egy üzenet mérete: 7 bájt (2 bájt adat + 5 bájt overhead)")
    print(f"- Üzenetek közti szünet: 1 bájt")
    print(f"- Teljes üzenetméret: 8 bájt")
    print(f"- Sávszélesség: 1 Mbit/sec = 125000 bájt/sec")
    print(f"\nSzámítások:")
    print(f"1. Egy üzenet továbbítási ideje: {message_time:.3f} ms")
    print(f"2. {B} ms alatt küldhető üzenetek száma: {max_events}")
    print(f"\nEredmény: A rendszer {max_events} állapotváltozó határérték")
    print(f"túllépését tudja időben ({B} ms alatt) jelezni.")
    
    # 1.2 Idővezérelt számítások
    print("\n1.2 IDŐVEZÉRELT MŰKÖDÉS")
    print("-" * 60)
    bandwidth, bytes_per_round, bytes_per_sec = calculate_time_driven(A, B)
    
    print(f"Adatok:")
    print(f"- Összes állapotváltozó száma: {A} × {B} = {A*B}")
    print(f"\nSzámítások:")
    print(f"1. Egy körben küldendő adatmennyiség:")
    print(f"   - Üzenetek: {A*B} × 7 bájt = {A*B*7} bájt")
    print(f"   - Szünetek: {A*B-1} × 1 bájt = {A*B-1} bájt")
    print(f"   - Összesen: {bytes_per_round} bájt")
    print(f"2. Másodpercenkénti adatmennyiség: {bytes_per_sec:.1f} bájt/sec")
    print(f"3. Szükséges sávszélesség: {bandwidth:.3f} Mbit/sec")
    
    print(f"\nEredmény: A minimálisan szükséges sávszélesség {bandwidth:.3f} Mbit/sec")

# Példa használat (az A és B értékeket itt lehet megadni)
A = 10  # példa érték
B = 45 # példa érték
print_results(A, B)