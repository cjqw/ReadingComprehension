all:
	python main.py --train_file ./data/train.txt \
        --dev_file ./data/dev.txt \
        --embedding_file ./embedding/glove.6B.100d.txt \
	--num_epoches 100 \
	--pre_trained model.pkl.gz \
	--eval_iter 150 \
	--batch_size 1

test:
	python main.py --train_file ./data/train.txt \
        --dev_file ./data/test.txt \
        --embedding_file ./embedding/glove.6B.100d.txt \
	--num_epoches 100 \
	--pre_trained model.pkl.gz \
	--eval_iter 150 \
	--test_only y \
	--batch_size 1
