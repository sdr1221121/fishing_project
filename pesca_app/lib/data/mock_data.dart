import '../models/document.dart';
import '../models/alert.dart';
import '../models/vessel.dart';


final mockVessel = Vessel(
  id: 1,
  name: "Mar Azul",
  registrationNumber: "LX-1234-P",
  capacity: 5,
  tonnage: 12.5,
);

final mockDocuments = [
  Document(
    id: 1,
    documentType: "Licença de Pesca",
    endDay: DateTime(2025, 12, 31),
    filePath: "/files/licenca_pesca.pdf",
    createDate: DateTime(2024, 1, 10),
  ),
  Document(
    id: 2,
    documentType: "Imposto de Circulação",
    endDay: DateTime(2025, 6, 30),
    filePath: "/files/imposto_circulacao.pdf",
    createDate: DateTime(2024, 2, 15),
  ),
];


final mockAlerts = [
  Alert(
    title: "Renovação da Licença de Pesca",
    description: "Expira em 5 dias.",
    date: DateTime.now().add(const Duration(days: 5)),
  ),
];
