import 'package:flutter/material.dart';
import '../models/document.dart';
import '../service/document_service.dart';
import 'package:open_file/open_file.dart';
import '../widgets/option_bottom.dart';

class DocumentScreen extends StatefulWidget {
  const DocumentScreen({super.key});
  @override
  State<DocumentScreen> createState() => _DocumentScreenState();
}

class _DocumentScreenState extends State<DocumentScreen> {
  List<Document> documents = [];
  bool isLoading = true;
  bool orderByNameAscending = true;

  @override
  void initState() {
    super.initState();
    loadDocuments();
  }

  Future<void> loadDocuments() async {
    final docs = await DocumentService.getDocuments();
    setState(() {
      documents = docs;
      isLoading = false;
    });
  }

  void sortDocuments() {
    setState(() {
      documents.sort((a, b) {
        return orderByNameAscending
            ? a.documentType.compareTo(b.documentType)
            : b.documentType.compareTo(a.documentType);
      });

      orderByNameAscending = !orderByNameAscending;
    });
  }

  /// AGRUPAR POR ANO
  Map<int, List<Document>> groupDocumentsByYear() {
    final Map<int, List<Document>> grouped = {};

    for (var doc in documents) {
      if (doc.endDay == null) continue;

      final year = doc.endDay!.year;

      if (!grouped.containsKey(year)) {
        grouped[year] = [];
      }
      grouped[year]!.add(doc);
    }

    // ordenar anos do mais recente para o mais antigo
    final sortedKeys = grouped.keys.toList()..sort((a, b) => b.compareTo(a));

    return {for (var key in sortedKeys) key: grouped[key]!};
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Documentos"),
        actions: [
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () {
              Navigator.pushNamed(context, "/upload_document")
                  .then((_) => loadDocuments());
            },
          ),

          IconButton(
            icon: Icon(orderByNameAscending
                ? Icons.sort_by_alpha
                : Icons.sort_by_alpha_outlined),
            onPressed: sortDocuments,
          ),
        ],
      ),

      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : documents.isEmpty
              ? const Center(child: Text("Nenhum documento encontrado."))
              : ListView(
                  padding: const EdgeInsets.all(16),
                  children: groupDocumentsByYear().entries.map((entry) {
                    final year = entry.key;
                    final docs = entry.value;

                    return Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        // Título da secção (ANO)
                        Padding(
                          padding: const EdgeInsets.symmetric(vertical: 8),
                          child: Text(
                            "$year",
                            style: const TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),

                        // Lista de documentos daquele ano
                        ...docs.map((document) {
                          return Card(
                            margin: const EdgeInsets.only(bottom: 12),
                            child: ListTile(
                              title: Text(document.documentType),
                              subtitle: Text(
                                "Expira: ${document.endDay?.toLocal().toString().split(" ")[0]}",
                              ),

                              onTap: () async {
                                if (document.filePath != null) {
                                  final result = await OpenFile.open(document.filePath!);

                                  if (result.type != ResultType.done) {
                                    ScaffoldMessenger.of(context).showSnackBar(
                                      SnackBar(
                                        content: Text(
                                          "Não foi possível abrir o documento: ${document.filePath}",
                                        ),
                                      ),
                                    );
                                  }
                                }
                              },

                              onLongPress: () {
                                showOptions(
                                  context: context,
                                  title: "Opções",
                                  options: [
                                    OptionItem(
                                      icon: Icons.delete,
                                      label: "Eliminar",
                                      onTap: () {
                                        // TODO: eliminar documento
                                      },
                                    ),
                                  ],
                                );
                              },
                            ),
                          );
                        }).toList(),
                      ],
                    );
                  }).toList(),
                ),
    );
  }
}
