<?php

namespace App\Models;

use Dcat\Admin\Traits\HasDateTimeFormatter;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class Department extends Model
{
	use HasDateTimeFormatter;
    use SoftDeletes;

    public function inspector(): hasMany
    {
        return $this->hasMany(Inspector::class);
    }

    }
