import '../models/document.dart';
import 'api_service.dart';
import 'package:http/http.dart' as http;

class DocumentService {
  static Future<List<Document>> getDocuments() async {
    try {
      final data = await ApiService.get("/documents/");
      return (data as List).map((json) => Document.fromJson(json)).toList();
    } catch (e) {
      print("Erro em getDocuments(): $e");
      rethrow;
    }
  }

  static Future<List<Document>> getLocalDocuments() async {
    try {
      final data = await ApiService.get("/documents/local/");
      return (data as List).map((json) => Document.fromJson(json)).toList();
    } catch (e) {
      print("Erro em getDocuments(): $e");
      rethrow;
    }
  }

  static Future<Document> getDocument(int id) async {
    try {
      final data = await ApiService.get("/documents/$id");
      return Document.fromJson(data);
    } catch (e) {
      print("Erro em getDocuments(): $e");
      rethrow;
    }
  }

  static Future<bool> uploadFile({
    required String filePath,
    required String documentType,
    required String endDay,
  }) async {
    try {
      final uri = Uri.parse("${ApiService.baseUrl}/documents/upload");

      var request = http.MultipartRequest("POST", uri);

      request.fields["document_type"] = documentType;
      request.fields["end_day"] = endDay;

      request.files.add(await http.MultipartFile.fromPath("file", filePath));

      final response = await request.send();

      return response.statusCode == 200;
    } catch (e) {
      print("Erro em uploadFile(): $e");
      rethrow;
    }
  }
}
