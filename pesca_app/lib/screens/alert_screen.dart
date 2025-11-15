import 'package:flutter/material.dart';
import '../data/mock_data.dart';
//import '../notifications/local_notifications.dart';

class AlertScreen extends StatelessWidget {
  const AlertScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Alertas")),
      body: ListView.builder(
        itemCount: mockAlerts.length,
        itemBuilder: (context, index) {
          final alert = mockAlerts[index];
          return Card(
            margin: const EdgeInsets.all(8),
            child: ListTile(
              title: Text(alert.title),
              subtitle: Text(alert.description),
              trailing: IconButton(
                icon: const Icon(Icons.alarm),
                onPressed: () {
                  //LocalNotifications.showNotification(alert.title, alert.description);
                },
              ),
            ),
          );
        },
      ),
    );
  }
}
