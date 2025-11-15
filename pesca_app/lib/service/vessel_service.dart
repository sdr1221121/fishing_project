import '../models/vessel.dart';
import 'api_service.dart';

class VesselService {

  // GET all vessels
  static Future<List<Vessel>> getVessels() async {
    final data = await ApiService.get("/vessels/");
    return (data as List).map((json) => Vessel.fromJson(json)).toList();
  }

  // GET vessel by ID
  static Future<Vessel> getVessel(int id) async {
    final data = await ApiService.get("/vessels/$id");
    return Vessel.fromJson(data);
  }

  // POST create vessel
  static Future<Vessel> createVessel(Vessel vessel) async {
    final body = {
      "name": vessel.name,
      "registration_number": vessel.registrationNumber,
      "capacity": vessel.capacity,
      "tonnage": vessel.tonnage,
    };

    final data = await ApiService.post("/vessels/", body);
    return Vessel.fromJson(data);
  }

  // DELETE vessel
  static Future<void> deleteVessel(int id) async {
    await ApiService.delete("/vessels/$id");
  }
}
