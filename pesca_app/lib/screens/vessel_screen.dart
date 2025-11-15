import 'package:flutter/material.dart';
import '../service/vessel_service.dart';
import '../models/vessel.dart';

class VesselScreen extends StatefulWidget {
  const VesselScreen({super.key});

  @override
  State<VesselScreen> createState() => _VesselScreenState();
}

class _VesselScreenState extends State<VesselScreen> {
  late Future<List<Vessel>> futureVessels;

  @override
  void initState() {
    super.initState();
    futureVessels = VesselService.getVessels(); // fetch vessels
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Embarcações")),
      body: FutureBuilder<List<Vessel>>(
        future: futureVessels,
        builder: (context, snapshot) {

          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(
              child: CircularProgressIndicator());
          }

          if (snapshot.hasError) {
            return Center(
              child: Text(
                "Erro ao carregar embarcações:\n${snapshot.error}",
                textAlign: TextAlign.center,
              ),
            );
          }

          final vessels = snapshot.data;

          if (vessels == null || vessels.isEmpty) {
            return const Center(child: Text("Nenhuma embarcação encontrada."));
          }

          return ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: vessels.length,
            itemBuilder: (context, index) {
              final vessel = vessels[index];

              return Card(
                margin: const EdgeInsets.only(bottom: 12),
                child: ListTile(
                  leading: const Icon(Icons.directions_boat),
                  title: Text(
                    vessel.name,
                    style: const TextStyle(fontWeight: FontWeight.bold),
                  ),
                  subtitle: Text(
                    "Matrícula: ${vessel.registrationNumber}"
                    "\nLotação: ${vessel.capacity} pessoas"
                    "\nArqueação Bruta: ${vessel.tonnage} GT",
                  ),
                  onTap: () {
                    // open details or edit vessel
                  },
                ),
              );
            },
          );
        },
      ),
    );
  }
}
