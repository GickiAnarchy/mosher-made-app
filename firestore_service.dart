import 'package:cloud_firestore/cloud_firestore.dart';
import '../models/employee.dart';

class FirestoreService {
  final FirebaseFirestore _db = FirebaseFirestore.instance;

  // Stream for real-time list updates
  Stream<List<Employee>> getEmployees() {
    return _db
        .collection('employees')
        .snapshots()
        .map(
          (snapshot) =>
              snapshot.docs.map((doc) => Employee.fromFirestore(doc)).toList(),
        );
  }

  // Replaces add_new_employee logic
  Future<void> addEmployee(String name, double wage) {
    return _db.collection('employees').add({
      'name': name,
      'wage': wage,
      'createdAt': FieldValue.serverTimestamp(),
    });
  }

  // Replaces log_shift logic
  Future<void> logShift({
    required String employeeId,
    required String employerId,
    required DateTime timeIn,
    required DateTime timeOut,
    String note = "",
  }) async {
    // Calculate hours (same as logic in timesheetmanager.py)
    double hours = timeOut.difference(timeIn).inMinutes / 60.0;
    if (hours < 0) hours += 24; // Handle overnight crossover

    // Get employee wage for logging
    DocumentSnapshot empDoc = await _db
        .collection('employees')
        .doc(employeeId)
        .get();
    double wage = (empDoc.data() as Map)['wage'] ?? 0.0;
    double amount = hours * wage;

    return _db.collection('logs').add({
      'employeeId': employeeId,
      'employerId': employerId,
      'timeIn': timeIn,
      'timeOut': timeOut,
      'hours': hours,
      'amount': amount,
      'note': note,
      'date': DateTime.now().toIso8601String().substring(0, 10),
    });
  }
}
