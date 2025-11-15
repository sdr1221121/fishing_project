class Vessel {
  final int id;
  final String name;
  final String registrationNumber;
  final double capacity;
  final double tonnage;

  Vessel({
    required this.id,
    required this.name,
    required this.registrationNumber,
    required this.capacity,
    required this.tonnage,
  });

  factory Vessel.fromJson(Map<String, dynamic> json) {
    return Vessel(
      id: json['id'],
      name: json['name'],
      registrationNumber: json['registration_number'],
      capacity: json['capacity'].toDouble(),
      tonnage: json['tonnage'].toDouble(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'registration_number': registrationNumber,
      'capacity': capacity,
      'tonnage': tonnage,
    };
  }
}