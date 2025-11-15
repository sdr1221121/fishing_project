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