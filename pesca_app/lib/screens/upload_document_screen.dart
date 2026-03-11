import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:pesca_app/service/document_service.dart';

class UploadDocumentScreen extends StatefulWidget {
  const UploadDocumentScreen({super.key});

  @override
  State<UploadDocumentScreen> createState() => _UploadDocumentScreenState();
}

class _UploadDocumentScreenState extends State<UploadDocumentScreen> {
  File? selectedFile;
  String? selectedType;
  DateTime? selectedDate;

  final List<String> documentTypes = [
    "Licença de Pesca",
    "Título de Propriedade",
    "Imposto de Circulação",
    "Declaração de Rendimentos",
    "Certificado de Segurança",
    "Outros",
  ];

  Future<void> pickDate() async {
    final now = DateTime.now();

    final date = await showDatePicker(
      context: context,
      initialDate: now,
      firstDate: DateTime(2000),
      lastDate: DateTime(2100),
      helpText: "Selecionar data de expiração",
    );

    if (date != null) {
      setState(() {
        selectedDate = date;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Carregar Documento")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [

            /// =============================
            /// Escolher o ficheiro
            /// =============================
            Center(
              child: ElevatedButton(
                onPressed: () async {
                  final picked = await FilePicker.platform.pickFiles();

                  if (picked == null) return;

                  setState(() {
                    selectedFile = File(picked.files.single.path!);
                  });
                },
                child: const Text("Selecionar Ficheiro"),
              ),
            ),

            if (selectedFile != null) ...[
              const SizedBox(height: 20),
              Text(
                "Ficheiro selecionado:",
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text(selectedFile!.path.split("/").last),
            ],

            const SizedBox(height: 30),

            /// Mostrar o resto APENAS depois de escolher o ficheiro
            if (selectedFile != null) ...[
              /// =============================
              /// Tipo de Documento
              /// =============================
              const Text(
                "Tipo de Documento",
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 6),
              DropdownButtonFormField<String>(
                decoration: const InputDecoration(border: OutlineInputBorder()),
                value: selectedType,
                items: documentTypes
                    .map((type) => DropdownMenuItem(
                          value: type,
                          child: Text(type),
                        ))
                    .toList(),
                onChanged: (v) => setState(() => selectedType = v),
              ),

              const SizedBox(height: 20),

              /// =============================
              /// Data de Expiração
              /// =============================
              const Text(
                "Data de Expiração",
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 6),

              InkWell(
                onTap: pickDate,
                child: Container(
                  padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 12),
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.grey),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        selectedDate == null
                            ? "Selecionar data"
                            : "${selectedDate!.day}/${selectedDate!.month}/${selectedDate!.year}",
                      ),
                      const Icon(Icons.calendar_month),
                    ],
                  ),
                ),
              ),

              const SizedBox(height: 30),

              /// =============================
              /// PASSO FINAL - Enviar
              /// =============================
              Center(
                child: ElevatedButton(
                  onPressed: () async {
                    if (selectedType == null) {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text("Selecione o tipo de documento.")),
                      );
                      return;
                    }

                    if (selectedDate == null) {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text("Selecione a data de expiração.")),
                      );
                      return;
                    }

                    await DocumentService.uploadDocumentFile(
                      selectedFile!,
                      selectedType!,
                      selectedDate!,
                    );

                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text("Documento enviado com sucesso!")),
                    );
                  },
                  child: const Text("Enviar Documento"),
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }
}