import { useState } from "react";
import api from "../services/api";

function ResumeUpload() {
  const [file, setFile] = useState(null);

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const token = localStorage.getItem("token");

      const res = await api.post(
        "/api/resume/upload",
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      alert(res.data.message);
    } catch (err) {
      console.error(err);
      alert("Upload Failed");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>Upload Resume</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={uploadResume}>
        Upload Resume
      </button>
    </div>
  );
}

export default ResumeUpload;