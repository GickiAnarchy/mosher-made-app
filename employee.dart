import 'package:cloud_firestore/cloud_firestore.dart';

class Employee {
  final String id;
  final String name;
  final double wage;

  Employee({required this.id, required this.name, required this.wage});

  factory Employee.fromFirestore(DocumentSnapshot doc) {
    Map data = doc.data() as Map<String, dynamic>;
    return Employee(
      id: doc.id,
      name: data['name'] ?? '',
      wage: (data['wage'] ?? 0).toDouble(),
    );
  }

  Map<String, dynamic> toMap() {
    return {'name': name, 'wage': wage};
  }
}
