import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';

class UploadDocumentScreen extends StatefulWidget {
  const UploadDocumentScreen({super.key});

  @override
  State<UploadDocumentScreen> createState() => _UploadDocumentScreenState();
}

class _UploadDocumentScreenState extends State<UploadDocumentScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Carregar Documento")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            const Text("Aqui vai o formulário para carregar documentos."),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () async {
                final picked = await FilePicker.platform.pickFiles();
              },
              child: const Text("Selecionar Arquivo"),
            ),
          ],
        ),
      ),
    );
  }
}
