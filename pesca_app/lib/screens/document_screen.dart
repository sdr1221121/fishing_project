import 'package:flutter/material.dart';
import '../models/document.dart';
import '../service/document_service.dart';
import 'package:open_file/open_file.dart';


class DocumentScreen extends StatefulWidget{
  const DocumentScreen({super.key});
  @override
  State<DocumentScreen> createState()=>_DocumentScreenState();
}

class _DocumentScreenState extends State<DocumentScreen>{
  late Future<List<Document>> futureDocuments;

  @override
  void initState() {
    super.initState();
    futureDocuments= DocumentService.getDocuments();
    print(futureDocuments);
  }

  void _refreshDocuments() {
    setState(() {
      futureDocuments = DocumentService.getDocuments();
    });
  }

  Future<void> _deleteDocument(BuildContext context, Document document) async {
    // Show confirmation dialog
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text("Confirmar Exclusão"),
        content: Text("Tem certeza que deseja excluir o documento '${document.documentType}'?"),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(false),
            child: const Text("Cancelar"),
          ),
          TextButton(
            onPressed: () => Navigator.of(context).pop(true),
            child: const Text("Excluir", style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      try {
        final success = await DocumentService.deleteDocument(document.id);
        if (success && context.mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text("Documento excluído com sucesso")),
          );
          _refreshDocuments();
        }
      } catch (e) {
        if (context.mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text("Erro ao excluir documento: $e")),
          );
        }
      }
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Documentos")),
      body: FutureBuilder<List<Document>>(
        future: futureDocuments,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting){
            return const Center (
              child: CircularProgressIndicator());
          }
          if(snapshot.hasError) {
            return Center(
              child: Text("Erro ao carregar documentos",textAlign: TextAlign.center
              ),
            );
          }
          final documents=snapshot.data;

          if (documents==null || documents.isEmpty){
            return const Center(
              child: Text("Nenhum documento encontrado."
              )
            );
          }
          return ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: documents.length,
            itemBuilder:(context, index){
              final document=documents[index];
              return Card(
                margin: const EdgeInsets.only(bottom: 12),
                child: ListTile(
                  title: Text(
                    document.documentType,
                  ),
                  subtitle: Text("Expira: ${document.endDay?.toLocal().toString().split(" ")[0]}"
                  ),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete, color: Colors.red),
                    onPressed: () => _deleteDocument(context, document),
                  ),
                  onTap: () async {
                    if(document.filePath != null) {
                      final result = await OpenFile.open(document.filePath!);
                      if (result.type != ResultType.done) {
                       ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text("Não foi possível abrir o documento. no diretorio local.")),
                       );
                      }
                   }
                  }
                ),
              );
            }
          );
        }
      ),
    );
  }
}

class DocumentDetailScreen extends StatelessWidget{
  final String path;

  const DocumentDetailScreen({super.key, required this.path});

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(title: const Text("Detalhes do Documento")),
      body: Center(child: Text("Caminho do Documento: $path"),),
    );
  }
}