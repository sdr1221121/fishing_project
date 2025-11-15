import 'package:flutter/material.dart';
import 'vessel_screen.dart';
import 'document_screen.dart';
import 'alert_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  final List<Widget> _screens = const [
    VesselScreen(),
    DocumentScreen(),
    AlertScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selectedIndex,
        onDestinationSelected: (index) => setState(() => _selectedIndex = index),
        destinations: const [
          NavigationDestination(icon: Icon(Icons.directions_boat), label: "Embarcação"),
          NavigationDestination(icon: Icon(Icons.description), label: "Documentos"),
          NavigationDestination(icon: Icon(Icons.notifications), label: "Alertas"),
        ],
      ),
    );
  }
}
