```markdown
# Face Position Predictor

This mini-project uses the Landing AI platform to predict the face positions (left, right, front) in images. The image dataset is sourced using the `icrawler` library, which downloads images directly from Google Images. The project is implemented in Python.

## Project Structure

- `main.py`: The main script to predict face positions using the Landing AI model.
- `download_images.py`: Script to download images from Google Images using the `icrawler` library.
- `images/`: Directory where the downloaded images are stored.
- `.env`: Environment file containing the API key for the Landing AI platform.
- `.gitignore`: Specifies which files and directories should be ignored by Git.

## Prerequisites

Ensure you have the following Python packages installed:

```bash
pip install pillow
pip install landingai
pip install icrawler
```

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sidharthd7/Face-Position-Predictor.git
    cd Face-Position-Predictor
    ```

2. **Set up the `.env` file**:
    Create a `.env` file in the root directory and add your Landing AI API key:
    ```
    API_KEY=your_landing_ai_api_key_here
    ENDPOINT_ID=your_landing_ai_endpoint_id_here
    ```

3. **Download images**:
    Run the `download_images.py` script to download images for training and testing:
    ```bash
    python download_images.py
    ```

4. **Predict face positions**:
    Run the `main.py` script to predict face positions in your images:
    ```bash
    python main.py
    ```

## Image Dataset

The images used for prediction are stored in the `dataset/` directory. You can organize them into sub-folders (e.g., `dataset/left`, `dataset/right`, `dataset/front`) based on their face positions.

## How It Works

1. **Image Download**: The `icrawler` library is used to scrape images from Google Images based on specific keywords (e.g., "face left position", "face right position", "face front position").

2. **Face Position Prediction**: The `Landing AI` model is utilized to predict the face position in the images. The model is called via the Landing AI SDK using the API key and endpoint ID provided.

## Contributing

Feel free to fork this project, submit issues, or create pull requests if you want to contribute or improve it.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Landing AI](https://landing.ai/) for providing the AI model platform.
- [icrawler](https://github.com/hellock/icrawler) for the image scraping library.
```
