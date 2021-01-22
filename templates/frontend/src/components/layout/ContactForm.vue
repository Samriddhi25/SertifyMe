<template>
  <form class="contact-form" @submit.prevent="sendMail">
    <div class="group-one">
      <div class="form-group">
        <label for="msg name">Email</label>
        <input
          type="text"
          id="msg-name"
          class="form-control"
          v-model="contactFormData.name"
        />
      </div>
      <div class="form-group">
        <label for="msg email">Name</label>
        <input
          type="text"
          id="msg-email"
          class="form-control"
          v-model="contactFormData.email"
        />
      </div>
    </div>
    <div class="form-group">
      <label for="msg message">Message</label>
      <textarea
        rows="7"
        id="msg-message"
        class="form-control-mess"
        v-model="contactFormData.message"
      ></textarea>
    </div>
    <div class="form-result">
      <p class="alert alert-success" v-if="success && !error">
        Message sent successfully.
      </p>
      <p class="alert alert-error" v-if="!success && error">Message failed.</p>
    </div>
    <div class="form-group">
      <button class="btn" type="submit">Send</button>
    </div>
  </form>
</template>

<script>
export default {
  name: "ContactForm",
  data: function () {
    return {
      contactFormData: {
        name: "",
        email: "",
        message: "",
      },
      success: false,
      error: false,
    };
  },
  methods: {
    sendMail: function () {
      // in a real app, it would be better if the URL is extracted as a env variable
      // const url = ' http://localhost:5001/vue-contact-form-3c668/us-central1/sendEmailCF';
      const { name, email, message } = this.contactFormData;
      const payload = { name, email, message };
      // console.log(JSON.stringify(payload));
      // fetch(url, {
      //     method: 'POST',
      //     headers: {
      //         'Content-Type': 'application/json',
      //     },
      //     body: JSON.stringify(payload)
      // })
      //     .then(() => {
      //         this.success = true;
      //         this.resetForm();
      //     })
      //     .catch(() => {
      //         this.error = true;
      //     })
    },
    resetForm: function () {
      this.contactFormData = {
        name: "",
        email: "",
        message: "",
      };
    },
  },
};
</script>

<style scoped>
.contact-form {
  padding: 20px;
  border-radius: 4px;
  width: 580px;
}
.group-one {
  display: flex;
  flex-direction: row;
}
.form-group {
  padding: 10px;
}
.form-control {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #6ea099;
  color: #25403f;
  border-radius: 4px;
  box-sizing: border-box;
}
.form-control-mess {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #6ea099;
  color: #25403f;
  font-size: 18px;
  border-radius: 4px;
  box-sizing: border-box;
}
input[type="text"].form-control {
  margin: 8px 0;
  display: inline-block;
}
textarea.form-control {
  resize: none;
}
/* .btn {
    cursor: pointer;
    padding: 8px 10px;
    outline: none;
    border: none;
    background: #3be249;
    font-size: 16px;
    width: 100%;
    border-radius: 4px;
    text-align: center;
} */
.msg {
  color: #25403f;
  font-weight: bolder;
}
.btn {
  cursor: pointer;
  font-size: 16px;
  width: 50%;
  margin-left: 25%;
  outline: none;
  text-align: center;
  color: #4a8280;
  padding: 10px 30px;
  border: 1px solid #4a8280;
  background-color: #0d1413;
  border-radius: 32.33px;
  text-decoration: none;
  font-weight: bold;
}
.btn:hover {
  color: #0d1413;
  border: 1px solid #0d1413;
  background-color: #4a8280;
}
.alert {
  padding: 0 10px;
}
.alert-success {
  color: #3be249;
}
.alert-error {
  color: #ff2121;
}
</style>