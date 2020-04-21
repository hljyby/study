const Profiles = require('../../modules/profiles')
const User = require('../../modules/user')

const express = require('express')
const router = express.Router()
const passport = require('passport')
const mongoose = require('mongoose')



const profilevalidator = require('../../vaildation/profiles.js')
const validateExperienceInput = require("../../vaildation/experience");
const validateEducationInput = require("../../vaildation/education");


router.get('/test', (req, res) => {
    res.json({
        msg: 'hellow world'
    })
})


router.get('/', passport.authenticate('jwt', {
    session: false
}), (req, res) => {
    let errors = {}
    Profiles.findOne({
            user: req.user.id
        })
        .populate('user', ["name", "avatar"])  //查user表把name和avatar放到ref里
        .then(fil => {
            if (!fil) {
                errors.profiles = '没有当前用户~'
                return res.status(404).json(
                    errors
                )
            }
            return res.json(fil)
        }).catch(err => res.json(err))
})

router.post('/', passport.authenticate('jwt', {
    session: false
}), (req, res) => {

    const {
        errors,
        isVaild
    } = profilevalidator(req.body)
    if (!isVaild) {
        return res.status(400).json(errors)

    }
    let profileFields = {}
    profileFields.user = req.user.id

    if (req.body.handle) {
        profileFields.handle = req.body.handle
    }
    if (req.body.company) {
        profileFields.company = req.body.company
    }
    if (req.body.website) {
        profileFields.website = req.body.website
    }
    if (req.body.location) {
        profileFields.location = req.body.location
    }
    if (req.body.status) {
        profileFields.status = req.body.status
    }
    if (req.body.bio) {
        profileFields.bio = req.body.bio
    }
    if (req.body.githubusername) {
        profileFields.githubusername = req.body.githubusername
    }
    if (req.body.skills !== undefined) {
        profileFields.skills = req.body.skills
    }
    profileFields.social = {}

    if (req.body.wechat) {
        profileFields.social.wechat = req.body.wechat
    }
    if (req.body.QQ) {
        profileFields.social.QQ = req.body.QQ
    }
    if (req.body.tengxunkt) {
        profileFields.social.tengxunkt = req.body.tengxunkt
    }
    if (req.body.wangyikt) {
        profileFields.social.wangyikt = req.body.wangyikt
    }
    Profiles.findOne({
        user: req.user.id
    }).then(fil => {
        console.log(fil)
        if (fil) {
            Profiles.findOneAndUpdate({
                user: req.user.id
            }, {
                $set: profileFields
            }, {
                new: true
            }).then(pro => {
                res.json(pro)
            })
        } else {
            Profiles.findOne({
                handle: profileFields.handle
            }).then(pro => {

                if (pro) {
                    errors.err = '您新创建的用户信息存在~'
                    res.status(400).json(errors)
                } else {
                    new Profiles(profileFields).save().then(fil => {
                        res.json(fil)
                    })
                }
            })
        }
    })
})


router.get('/handle/:handle', (req, res) => {
    let errors = {}
    Profiles.findOne({
        handle: req.params.handle
    }).populate('user', ['name', 'avatart']).then(file => {
        if (!file) {
            res.status(404).json(
                errors.nofile = '没有实例'
            )
        } else {
            res.json(file)
        }
    })
})

router.get('/user/:user_id', (req, res) => {
    let errors = {}
    Profiles.findOne({
        user: req.params.user_id
    }).populate('user', ['name', 'avatart']).then(file => {
        if (!file) {
            res.status(404).json(
                errors.nofile = '没有实例'
            )
        } else {
            res.json(file)
        }
    })
})

router.get('/all', (req, res) => {
    let errors = {}
    Profiles.find().populate('user', ['name', 'avatart']).then(file => {
        if (!file) {
            res.status(404).json(
                errors.nofile = '没有实例'
            )
        } else {
            res.json(file)
        }
    })
})


router.post("/experience", passport.authenticate('jwt', {
    session: false
}), (req, res) => {
    const {
        errors,
        isValid
    } = validateExperienceInput(req.body);

    // 判断isValid是否通过
    if (!isValid) {
        return res.status(400).json(errors);
    }

    Profiles.findOne({
            user: req.user.id
        })
        .then(profile => {
            const newExp = {
                title: req.body.title,
                company: req.body.company,
                location: req.body.location,
                from: req.body.from,
                to: req.body.to,
                current: req.body.current,
                description: req.body.description,
            }

            profile.experience.unshift(newExp);

            profile.save().then(profile => res.json(profile));
        })
})



router.post("/education", passport.authenticate('jwt', {
    session: false
}), (req, res) => {
    const {
        errors,
        isValid
    } = validateEducationInput(req.body);

    // 判断isValid是否通过
    if (!isValid) {
        return res.status(400).json(errors);
    }

    Profiles.findOne({
            user: req.user.id
        })
        .then(profile => {
            const newEdu = {
                school: req.body.school,
                degree: req.body.degree,
                fieldofstudy: req.body.fieldofstudy,
                from: req.body.from,
                to: req.body.to,
                current: req.body.current,
                description: req.body.description,
            }

            profile.education.unshift(newEdu);

            profile.save().then(profile => res.json(profile));
        })
})


router.delete("/experience/:epx_id", passport.authenticate('jwt', {
    session: false
}), (req, res) => {

    Profiles.findOne({
            user: req.user.id
        })
        .then(profile => {
            const removeIndex = profile.experience
                .map(item => item.id)
                .indexOf(req.params.epx_id);

            profile.experience.splice(removeIndex, 1);

            profile.save().then(profile => res.json(profile));
        })
        .catch(err => res.status(404).json(err));
})

router.delete("/education/:edu_id", passport.authenticate('jwt', {
    session: false
}), (req, res) => {

    Profiles.findOne({
            user: req.user.id
        })
        .then(profile => {
            const removeIndex = profile.experience
                .map(item => item.id)
                .indexOf(req.params.epx_id);

            profile.education.splice(removeIndex, 1);

            profile.save().then(profile => res.json(profile));
        })
        .catch(err => res.status(404).json(err));
})

router.delete("/all", passport.authenticate('jwt', {
    session: false
}), (req, res) => {

    Profiles.findOneAndRemove({
            user: req.user.id
        })
        .then(() => {
            User.findOneAndRemove({
                    _id: req.user.id
                })
                .then(() => {
                    res.json({
                        success: true
                    })
                })
        })
})
module.exports = router