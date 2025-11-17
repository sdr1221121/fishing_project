import 'dart:io';
import 'package:path_provider/path_provider.dart';

class FileManeger {
  static Future<String> saveFileLocally(File file) async {
    final directory = await getApplicationDocumentsDirectory();

    final fileName =file.uri.pathSegments.last;

    final newPath = "${directory.path}/$fileName";
    final newFile = File(newPath);

    await newFile.writeAsBytes(await file.readAsBytes());

    return newPath;
  }
}
