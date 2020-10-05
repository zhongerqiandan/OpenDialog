from dataset_init import *
from models import *

dataset_loader = {
    'DualLSTM': load_ir_dataset,
    'seq2seq': load_seq2seq_dataset,
    'kwgpt2': load_kwgpt2_dataset,
    'gpt2': load_gpt2_dataset,
    'gpt2v2': load_gpt2v2_dataset,
    'pone': load_pone_dataset,
    'pfgpt2': load_pfgpt2_dataset,
    'when2talk': load_when2talk_dataset,
    'gpt2retrieval': load_gpt2retrieval_dataset,
    'gpt2lm': load_gpt2lm_dataset,
    'gpt2gan': load_gpt2rl_dataset,
    'multigpt2': load_multigpt2_dataset,
    'bertretrieval': load_bert_ir_dataset,
    'lccc': load_lccc_dataset,
    'bertretrieval_multiview': load_bert_ir_multiview_dataset,
    'bertretrieval_cl': load_bert_ir_cl_dataset,
    'bertmc': load_bert_ir_mc_dataset,
    'bertirbi': load_bert_irbi_dataset,
    'transformer': load_seq2seq_trs_dataset,
}

agent_map = {
    'DualLSTM': DualLSTMAgent, 
    'seq2seq': Seq2SeqAgent,
    'gpt2': GPT2Agent,
    'gpt2v2': GPT2V2Agent,
    'gpt2retrieval': GPT2RetrievalAgent,
    'pfgpt2': PFGPT2Agent,
    'kwgpt2': KWGPT2Agent,
    'gpt2_mmi': GPT2Agent,
    'when2talk': When2TalkAgent,
    'gpt2lm': GPT2Agent,
    'multigpt2': MultiGPT2Dataset,
    'bertretrieval': BERTRetrievalAgent,
    'bertretrieval_multiview': BERTRetrievalAgent,
    'bertretrieval_cl': BERTRetrievalCLAgent,
    'bertlogic': BERTRetrievalAgent,
    'bertnli': BERTNLIAgent,
    'gpt2gan': GPT2RLAgent,
    'gpt2gan_v2': GPT2RLAgent_V2,
    'pone': PONEAgent,
    'bertmc': BERTMCAgent,
    'lccc': LCCCFTAgent,
    'bertretrieval_dis': BERTRetrievalDISAgent,
    'lcccir': LCCCIRAgent,
    'uni': UNIAgent,
    'bert_na': BERTNAAgent,
    'bertirbi': BERTBiEncoderAgent,
    'transformer': TransformerAgent,
}

# run_mode is the keyname of the agent, mode is the key in the args
model_parameters = {
    'DualLSTM': [('multi_gpu',), {'run_mode': 'mode', 'lang': 'lang'}],
    'bertretrieval': [('multi_gpu',), {'run_mode': 'mode', 'lang': 'lang', 'local_rank': 'local_rank'}],
    'lccc': [('multi_gpu',), {'run_mode': 'mode'}],
    'bertmc': [('multi_gpu',), {'run_mode': 'mode', 'lang': 'lang', 'model_type': 'mc'}],
    'bertmc': [('multi_gpu',), {'run_mode': 'mode', 'lang': 'lang', 'model_type': 'mcf'}],
    'seq2seq': [('multi_gpu', 'vocab'), {'run_mode': 'mode', 'lang': 'lang', 'local_rank': 'local_rank'}],
    'gpt2': [('total_steps', 'multi_gpu'), {'run_mode': 'mode', 'lang': 'lang', 'local_rank': 'local_rank'}],
    'gpt2v2': [('total_steps', 'multi_gpu'), {'run_mode': 'mode', 'lang': 'lang', 'local_rank': 'local_rank'}],
    'gpt2gan': [('multi_gpu',), {'run_mode': 'mode', 'lang': 'lang'}],
    'transformers': [('total_steps', 'multi_gpu'), {'run_mode': 'mode', 'lang': 'lang', 'local_rank': 'local_rank' 'vocab': 'vocab'}],
}

# ========== load the config by the utils functions ========== #
def collect_parameter_4_model(args):
    if args['model'] in model_parameters:
        parameter_map, parameter_key = model_parameters[args['model']]
        parameter_map = [args[key] for key in parameter_map]
        parameter_key = {key: args[value] for key, value in parameter_key.items()}
        return parameter_map, parameter_key
    else:
        raise Exception(f'[!] cannot find the model {args["model"]}')
        
def load_dataset(args):
    if args['model'] in dataset_loader:
        return dataset_loader[args['model']](args)
    else:
        raise Exception(f'[!] cannot find the model {args["model"]}')