from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def check_t5():
    try:
        # Check if PyTorch works
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")  # Should be False if CPU-only
        
        # Try loading T5-small
        print("\nLoading T5-small model...")
        model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
        tokenizer = AutoTokenizer.from_pretrained("t5-small")
        
        # Test inference
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        test_text = "The quick brown fox jumps over the lazy dog. " * 5
        summary = summarizer("summarize: " + test_text, max_length=50)
        
        print("\n✅ T5-small is working!")
        print(f"Test summary: {summary[0]['summary_text']}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    check_t5()