o
    ���e=  �                   @   s   ddd�Z dS )�{�G�z�?�G�z��?c           	      C   sL   | | }|� |�}|� |�}| ||k ||kB  }| ||k||k @  }||fS )N)�quantile)	�data�feature�left�right�x�lower_bound�upper_bound�outliers�cleaned� r   �g/home/elena/Repository/BLOCK_1/BONUS_Marcdown_and_Git/DataCleaningProject/outliers_lib/find_outliers.py�find_outliers_quantile   s   

r   N)r   r   )r   r   r   r   r   �<module>   s    