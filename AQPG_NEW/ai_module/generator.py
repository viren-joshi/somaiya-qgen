from transformers import T5Tokenizer, T5ForConditionalGeneration,T5Model
import torch

model = T5ForConditionalGeneration.from_pretrained("C:\\Users\\taaha\\OneDrive\\Desktop\\AQPG_NEW\\save_model")
tokenizer = T5Tokenizer.from_pretrained("C:\\Users\\taaha\\OneDrive\\Desktop\\AQPG_NEW\\save_model")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def get_questions(paragraph):
  bt_levels = ['Remember', 'Understand', 'Apply', 'Analyse', 'Evaluate', 'Create']
  ans = {}
  for bt_level in bt_levels:
      input_text = f'{bt_level}: {paragraph} {tokenizer.eos_token}'
      input_ids = tokenizer.encode(input_text, max_length=512, padding='max_length', truncation=True, return_tensors='pt').to(device)
      model.eval()
      generated_ids = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True).to(device)
      output_text = tokenizer.decode(generated_ids.squeeze(), skip_special_tokens=True).lstrip('\n')
      output_text = output_text.split(' ', 1)[1]
      print(f'{bt_level} level question: {output_text}')
      ans[bt_level] = output_text
      

  return ans
      
# x = '''
# There are different ways to categorize operating systems, but one common approach is to classify them into seven broad types based on their characteristics and features:

# Batch Operating System: A batch operating system processes a series of jobs in a batch mode, without any user interaction. It is suitable for applications that require long processing times and do not require frequent user intervention.

# Time-Sharing Operating System: A time-sharing operating system allows multiple users to access a computer system simultaneously and share its resources. Each user gets a time slice of the CPU, and the system switches between them rapidly to give the illusion of concurrent execution.

# Distributed Operating System: A distributed operating system manages a group of networked computers as a single system, enabling users to access resources and data from any location. It allows for efficient resource sharing and scalability.

# Network Operating System: A network operating system provides features to manage and operate a network of computers, such as file sharing, printer sharing, and security. It typically runs on a dedicated server and manages client computers.

# Real-Time Operating System: A real-time operating system is designed to process tasks with strict time constraints, such as those in industrial control systems, robotics, and multimedia applications. It guarantees timely response to events and interrupts.

# Mobile Operating System: A mobile operating system is designed for mobile devices, such as smartphones and tablets. It provides features such as touch screen interface, wireless connectivity, and location-based services.

# Embedded Operating System: An embedded operating system runs on specialized devices, such as routers, digital cameras, and medical equipment. It is optimized for low power consumption, small memory footprint, and real-time performance.
# '''
# get_questions(x)