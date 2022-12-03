from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

RareAA = {
    'B': ['D', 'N'],
    'Z': ['E', 'Q'],
    'J': ['I', 'L'],
    'O': [''],
    'U': ['C'],
    'X': ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
}
def Modeler(Sequence, RareAA , rareAA_char):
    """
    Handle specific amino acid characters in a given sequence
    :param Sequence: Amino Acid sequence records
    :param RareAA Amino Acid dictionary
    :param rareAA_char rare amino acid list
    """
    Seq_list = []
    for Seqinfo in Sequence:
        if rareAA_char in Seqinfo.seq:
            for AA in RareAA[rareAA_char]:
                New_seq = Seqinfo.seq.replace(rareAA_char, AA)
                New_id = Seqinfo.id + "_" + rareAA_char + "_" + AA
                record = SeqRecord(seq=Seq(New_seq), id=New_id, description="")
                Seq_list.append(record)
    return Seq_list

def ModelSequence(Sequence):
    """
    Handle specific amino acid characters in a given sequence
    :param Sequence: Amino Acid sequence
    """
    Sequence_list = []

    RareAA_list = list(filter(lambda x: x in Sequence, RareAA.keys()))
    if len(RareAA_list) == 0:
        Sequence_list.append(record)
        return Sequence_list

    Sequence_list.append(Sequence)
    Sequence_list = Modeler(Sequence_list, RareAA, 'X')
    Sequence_list = Modeler(Sequence_list, RareAA, 'B')
    Sequence_list = Modeler(Sequence_list, RareAA, 'Z')
    Sequence_list = Modeler(Sequence_list, RareAA, 'J')
    Sequence_list = Modeler(Sequence_list, RareAA, 'O')
    Sequence_list = Modeler(Sequence_list, RareAA, 'U')

    return Sequence_list

Seq_list_All = []
fasta_sequences = SeqIO.parse(open("test.fasta"),'fasta')
for record in fasta_sequences:
    Returned_List = ModelSequence(record)
    Seq_list_All.extend(Returned_List)

SeqIO.write(Seq_list_All, "test_Processed.fasta", "fasta")