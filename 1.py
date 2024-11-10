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
    BITS_PER_MESSAGE = 768        # 720 bit payload + 40 bit overhead + 8 bit gap
    DEADLINE_SEC = B/1000         # B ms = B/1000 sec
    
    bandwidth_bits_sec = (A * BITS_PER_MESSAGE) / DEADLINE_SEC
    bandwidth_kbits_sec = bandwidth_bits_sec / 1000
    
    return bandwidth_kbits_sec, BITS_PER_MESSAGE

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
    bandwidth_kbits, bits_per_message = calculate_time_driven(A, B)
    
    print(f"Adatok:")
    print(f"- Csomópontok száma (A): {A}")
    print(f"- Előírt határidő (B): {B} ms = {B/1000} sec")
    print(f"- Egy üzenet felépítése:")
    print(f"  * Payload: 45 × 16 = 720 bit")
    print(f"  * Overhead: 40 bit")
    print(f"  * Intermessage Gap: 8 bit")
    print(f"  * Összesen: {bits_per_message} bit")
    
    print(f"\nSzámítások:")
    print(f"Minimális sávszélesség = (csomópontok száma × üzenethossz) / előírt határidő")
    print(f"                       = ({A} × {bits_per_message}) / {B/1000}")
    print(f"                       = {A * bits_per_message} / {B/1000}")
    print(f"                       ≈ {bandwidth_kbits:.2f} kbit/sec")
    
    print(f"\nEredmény: A minimálisan szükséges sávszélesség {bandwidth_kbits:.2f} kbit/sec")    

# Példa használat (az A és B értékeket itt lehet megadni)
A = 5  # példa érték
B = 45 # példa érték
print_results(A, B)